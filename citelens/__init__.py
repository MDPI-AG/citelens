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

from .dto import Article, CitationItem, SimilarityResult
from .lib import decode_input_file, embed_article, embed_text, embedding_similarity, process_item

__all__ = [
    "Article",
    "CitationItem",
    "SimilarityResult",
    "decode_input_file",
    "embed_article",
    "embed_text",
    "embedding_similarity",
    "process_item",
]
