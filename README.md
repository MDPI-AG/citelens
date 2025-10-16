# Cite Lens: An AI Tool for Detecting Out-of-Scope and Out-of-Context Citations

Cite Lens is an AI-powered tool to measure the relevance of citations in scientific papers using semantic similarity.
The concept was developed by MDPI AG, and presented at the
[TPDL 2025 conference](https://tpdl2025.github.io/), [doi.org/10.1007/978-3-032-06136-2_3](doi.org/10.1007/978-3-032-06136-2_3).

This repository contains a commandline tool (CLI) that performs the similarity computation used in the publication.
It uses the open source embedding model Specter downloaded from Hugging Face.
The commandline tool is designed to read
a JSON file with citation items, each composed of

* the citing article title and abstract,
* the citing context (usually a sentence or paragraph), and
* the title and abstract of the reference article.

The dataset of open access articles used in this work is available [here](https://huggingface.co/datasets/mdpi-ai/citelens). Cited articles are not included due to potential copyright restrictions.

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
    "article_reference_alert": false,
    "context_reference": 0.7734495997428894,
    "context_reference_alert": false,
    "publisher": "Publisher A",
    "journal": "Journal A"
  },
  {
    "id": 2,
    "article_reference": 0.8086146116256714,
    "article_reference_alert": false,
    "context_reference": 0.7901187539100647,
    "context_reference_alert": false,
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


We provide an example of an [article](https://doi.org/10.1007/s12517-022-10107-4) retracted for out-of-scope citation [json file](./real_case_example.json). We also include in this example Json a proper reference as a comparison.

## Run example

```bash
uv run citelens ./example.json
```

## Development and contributing

To contribute to the development of Cite Lens, you can clone the repository and run the following commands:

```bash
git clone https://github.com/MDPI-AG/citelens.git
cd citelens
make install
make install_pre_commit
uv run citelens --help
```

If you use this work in your research, please consider citing us:

```bibtex
@InProceedings{10.1007/978-3-032-06136-2_3,
author="Broise, Jean-Baptiste de la
and Sauerburger, Frank
and Sayas, Enric
and Tecu, Dan-Marin
and Meijere, Sanita
and Cuculovic, Milos",
editor="Balke, Wolf-Tilo
and Golub, Koraljka
and Manolopoulos, Yannis
and Stefanidis, Kostas
and Zhang, Zheying
and Aalberg, Trond
and Manghi, Paolo",
title="Cite Lens: An AI Tool for Detecting Out-of-Scope and Out-of-Context Citations",
booktitle="New Trends in Theory and Practice of Digital Libraries",
year="2026",
publisher="Springer Nature Switzerland",
address="Cham",
pages="25--34",
isbn="978-3-032-06136-2"
}
```

 
