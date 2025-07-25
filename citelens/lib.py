# Cite Lens: An AI Tool for Detecting Out-of-Scope and Out-of-Context Citations
# Copyright (C) 2025 MDPI AG

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
from functools import lru_cache
from typing import TextIO

import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer

from citelens.dto import Article, CitationItem, SimilarityResult


@lru_cache(maxsize=1)
def get_tokenizer_model() -> tuple[AutoTokenizer, AutoModel]:
    """Load the Specter model and tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained("allenai/specter")
    model = AutoModel.from_pretrained("allenai/specter")

    return tokenizer, model


def embed_text(text: str) -> np.ndarray:
    """Embed the given text using the Specter model."""
    tokenizer, model = get_tokenizer_model()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[0, 0, :].numpy()


def embed_article(article: Article) -> np.ndarray:
    """Embed the given article using the Specter model."""
    return embed_text(article.title + "\n" + (article.abstract or ""))


def embedding_similarity(embedding1: np.ndarray, embedding2: np.ndarray) -> float:
    """Compute the cosine similarity between two embeddings."""
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))


def decode_input_file(file: TextIO) -> list[CitationItem]:
    """Decode the input file containing citation items."""
    items = []
    for i, item in enumerate(json.load(file)):
        try:
            items.append(CitationItem(**item))
        except ValueError as e:
            raise ValueError(f"Error decoding item {i}: {e}") from e

    return items


def process_item(item: CitationItem) -> SimilarityResult:
    """Process a single citation item and compute similarity results."""
    paper_embedding = embed_article(item.paper)
    reference_embedding = embed_article(item.reference)
    context_embedding = embed_text(item.context)

    article_reference_similarity = embedding_similarity(paper_embedding, reference_embedding)
    context_reference_similarity = embedding_similarity(context_embedding, reference_embedding)

    return SimilarityResult(
        id=item.id,
        article_reference=article_reference_similarity,
        context_reference=context_reference_similarity,
        publisher=item.publisher,
        journal=item.journal,
    )
