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

from pydantic import BaseModel, Field


class Article(BaseModel):
    """Model representing an article with title, abstract, and optional DOI."""

    title: str
    abstract: str | None = None
    doi: str | None = None


class CitationItem(BaseModel):
    """Model representing a citation item with paper, reference, context, and optional publisher and journal.

    A article-reference similarity and context-reference similarity will be computed for each item.
    """

    id: int = Field(description="Arbitrary ID to match citation items with computed similarity results")
    paper: Article
    reference: Article
    context: str | None = None
    publisher: str | None = None
    journal: str | None = None


class SimilarityResult(BaseModel):
    """Model representing the similarity results for a citation item."""

    id: int = Field(description="Arbitrary ID to match citation items with computed similarity results")
    article_reference: float = Field(
        description="Embedding similarity between the citing article (article) and the cited article (reference)."
    )
    article_reference_alert: bool = Field(
        description="Whether the article-reference similarity is below the detection threshold."
    )
    context_reference: float | None = Field(
        description="Embedding similarity between the paragraph where the citation appears (context) and the cited article (reference)."
    )
    context_reference_alert: bool | None = Field(
        description="Whether the context-reference similarity is below the detection threshold."
    )
    publisher: str | None = None
    journal: str | None = None

    def __str__(self):
        """String representation used when printing to stdout."""
        res_str = f"Item {self.id: 6d}: {self.publisher or ''} {self.journal or ''}\n"
        res_str += f"    article-reference similarity {self.article_reference:.3f} {'(ALERT!)' if self.article_reference_alert else ''}\n"
        if self.context_reference is not None:
            res_str += f"    context-reference similarity {self.context_reference:.3f} {'(ALERT!)' if self.context_reference_alert else ''}\n"
        return res_str
