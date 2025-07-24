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

TBC

## Input format

TBD

## Development and contributing

To contribute to the development of Cite Lens, you can clone the repository and run the following commands:

```bash
git clone https://github.com/MDPI-AG/citelens.git
cd citelens
make install
uv run citelens --help
```