from unittest.mock import patch

import numpy as np
from pytest import approx

import citelens
from tests import mock


@patch("citelens.embed_text", mock.embed_text)
def test_mock():
    """Test the mock embedding function."""
    text = "This is a test."
    embedding = citelens.embed_text(text)

    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (32,)
    assert embedding.dtype == np.float32


def test_embed_test_real():
    """Test the real embedding function."""
    text = "This is a test."
    embedding = citelens.embed_text(text)

    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (768,)
    assert embedding.dtype == np.float32

    # Test two hard-coded values
    assert embedding[0] == approx(-0.449, abs=1e-3)
    assert embedding[1] == approx(0.636, abs=1e-3)


@patch("citelens.lib.embed_text", mock.embed_text)
def test_embed_article_no_abstract():
    """Test embedding an article without an abstract."""
    article = citelens.Article(title="Test title", abstract=None)
    embedding = citelens.embed_article(article)

    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (32,)
    assert embedding.dtype == np.float32


@patch("citelens.lib.embed_text", mock.embed_text)
def test_embed_article_with_abstract():
    """Test embedding an article with an abstract."""
    article = citelens.Article(title="Test title", abstract="Test abstract")
    embedding = citelens.embed_article(article)

    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (32,)
    assert embedding.dtype == np.float32


@patch("citelens.lib.embed_text", mock.embed_text)
def test_embedding_similarity_identical():
    """Check that the same article has a similarity of 1."""
    embedding = np.array([1.0, 2.0, 3.0, -4.0, -5.0])

    assert citelens.embedding_similarity(embedding, embedding) == approx(1.0)


@patch("citelens.lib.embed_text", mock.embed_text)
def test_embedding_similarity_similar():
    """Check that the two similar articles have a similarity close to 1."""
    embedding1 = np.array([1.0, 2.0, 3.0, -4.0, -5.0])
    embedding2 = np.array([1.0, 2.0, 3.0, -4.0, -5.1])

    assert citelens.embedding_similarity(embedding1, embedding2) == approx(1.0, abs=1e-3)


@patch("citelens.lib.embed_text", mock.embed_text)
def test_embedding_similarity_orthogonal():
    """Check that two orthogonal articles have a similarity of 0."""
    embedding1 = np.array([1.0, 2.0, 0.0])
    embedding2 = np.array([2.0, -1.0, 0.0])

    assert citelens.embedding_similarity(embedding1, embedding2) == approx(0.0, abs=1e-3)


@patch("citelens.lib.embed_text", mock.embed_text)
def test_embedding_similarity_antipolar():
    """Check that antipolar articles have a similarity of -1."""
    embedding1 = np.array([1.0, 2.0, 3.0, -4.0, -5.0])
    embedding2 = np.array([-1.0, -2.0, -3.0, 4.0, 5.0])

    assert citelens.embedding_similarity(embedding1, embedding2) == approx(-1.0, abs=1e-3)
