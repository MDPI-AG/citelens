import json
from io import StringIO

import pytest

import citelens


def test_decode_input_single_input():
    """Test decoding a single citation item."""
    buffer = StringIO()
    json.dump(
        [
            {
                "id": 1,
                "paper": {"title": "Test Paper", "abstract": "This is a test abstract.", "doi": "10.1000/test"},
                "reference": {"title": "Test Reference", "abstract": None, "doi": None},
                "context": "This is the context of the citation.",
                "publisher": "Test Publisher",
                "journal": "Test Journal",
            }
        ],
        buffer,
    )
    buffer.seek(0)

    (item,) = citelens.decode_input_file(buffer)

    assert item.id == 1
    assert item.paper.title == "Test Paper"
    assert item.paper.abstract == "This is a test abstract."
    assert item.reference.title == "Test Reference"
    assert item.reference.abstract is None
    assert item.context == "This is the context of the citation."
    assert item.publisher == "Test Publisher"
    assert item.journal == "Test Journal"


def test_decode_input_invalid_json():
    """Test decoding raises ValueError on invalid JSON."""
    buffer = StringIO()
    buffer.write("[Invalid JSON]")
    buffer.seek(0)

    with pytest.raises(ValueError):
        citelens.decode_input_file(buffer)


def test_decode_invalid_schema():
    """Test decoding invalid schema raises ValueError."""
    buffer = StringIO()
    json.dump(
        [
            {
                "id": 1,
                "paper": {"titlex": "Test Paper", "abstract": "This is a test abstract.", "doi": "10.1000/test"},
                "reference": {
                    "abstract": 32,
                },
                "context": "This is the context of the citation.",
            }
        ],
        buffer,
    )
    buffer.seek(0)

    with pytest.raises(ValueError):
        citelens.decode_input_file(buffer)
