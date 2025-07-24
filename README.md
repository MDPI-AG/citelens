# Cite Lens: An AI Tool for Detecting Out-of-Scope and Out-of-Context Citations 

Cite Lens is an AI-powered tool to measure the relevance of citations in scientific papers using semantic similarity.
The concept was developed by MDPI AG, a leading open access publisher, and presented at the
[TPDL 2025 conference](https://tpdl2025.github.io/).

This repository contains a commandline tool (CLI) that performs the similarity computation used in the publication.
It uses the open source embedding model Specter downloaded from Hugging Face.
The commandline tool is designed to read
a JSON file with citation items, each composed of
* the citing article title and abstract,
* the citing context (usually a sentence or paragraph), and
* the title and abstract of the reference article.

The dataset used for the publication at TPDL 2025 is not shared with the tool in this repository.
Although the papers used in the analysis are open access, the cited articles might be subject
to restrictive copyright licenses and cannot be made available.

## Installation

You can install the Cite Lens CLI as a `uv` tool (recommended)
```bash
uv tool install https://github.com/MDPI-AG/citelens/archive/refs/heads/master.zip
```

or as a Python package with `pip`:

```bash
pip install https://github.com/MDPI-AG/citelens/archive/refs/heads/master.zip
```

## Usage

The CLI tool `citelens` can be used to process a JSON file containing citation items. If no output file is specified, the results are printed to standard output (stdout).

```bash
$ citelens example.json
Item      1: Publisher A Journal A
    article-reference similarity 0.870
    context-reference similarity 0.773

Item      2: Publisher B Journal B
    article-reference similarity 0.809
    context-reference similarity 0.790
```


Alternatively, the output can be written to a file:

```bash
$ citelens example.json output.json
$ cat output.json
[
  {
    "id": 1,
    "article_reference": 0.8704640865325928,
    "context_reference": 0.7734495997428894,
    "publisher": "Publisher A",
    "journal": "Journal A"
  },
  {
    "id": 2,
    "article_reference": 0.8086146116256714,
    "context_reference": 0.7901187539100647,
    "publisher": "Publisher B",
    "journal": "Journal B"
  }
]
```

### Input format

The input format is a list of `CitationItem`s as defined in `citelens/dto.py`. Each item should contain the following fields:

- `id`: An arbitrary ID to match citation items with computed similarity results.
- `paper`: An `Article` object representing the citing article.
- `reference`: An `Article` object representing the cited article.
- `context`: The text of the paragraph where the citation appears.
- `publisher`: The publisher of the cited article (optional).
- `journal`: The journal of the cited article (optional).

For each citation item, the tool computes two similarity scores:
- `article_reference`: Similarity between the citing article and the cited article.
- `context_reference`: Similarity between the citing context and the cited article.

### Example input file

An input file might look like `example.json`.

```json
[{
    "id": 1,
    "paper": {
        "title": "Test Paper",
        "abstract": "This is a test abstract.",
        "doi": "10.1000/test"
    },
    "reference": {
        "title": "Test Reference",
        "abstract": null,
        "doi": null
    },
    "context": "This is the context of the citation.",
    "publisher": "Publisher A",
    "journal": "Journal A"
}, {
    "id": 2,
    "paper": {
        "title": "Another Paper",
        "abstract": "This is another test abstract.",
        "doi": "10.1000/other"
    },
    "reference": {
        "title": "Some other reference",
        "abstract": "On the same other optic",
        "doi": "10.1000/someother"
    },
    "context": "This is the context of the citation.",
    "publisher": "Publisher B",
    "journal": "Journal B"
}]
```



## Development and contributing

To contribute to the development of Cite Lens, you can clone the repository and run the following commands:

```bash
git clone https://github.com/MDPI-AG/citelens.git
cd citelens
make install
uv run citelens --help
```