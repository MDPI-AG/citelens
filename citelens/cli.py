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
from pathlib import Path
from typing import Annotated

from tqdm import tqdm
from typer import Argument, Option, Typer

from .lib import decode_input_file, process_item

app = Typer()


@app.command()
def citelens(
    input_file: Annotated[Path, Argument(help="Path to the input file containing citation information.")],
    output_file: Annotated[str, Argument(help="Path to the output file")] = "-",
    progress: Annotated[
        bool, Option(help="Show progress bar for processing items. Ignore if output is stdout.")
    ] = True,
):
    """Cite Lens: An AI Tool for Detecting Out-of-Scope and Out-of-Context Citations.

    The input file should contain citation items with information about a paper, a reference, and its citation context.
    The output will be saved to the specified output file or printed to stdout if no output file is provided.



    Copyright (C) 2025 MDPI AG

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """
    # Read and decode the input file
    with open(input_file) as infile:
        items = decode_input_file(infile)

    # If printing to stdout, process items directly
    if output_file == "-":
        for item in items:
            print(process_item(item))
        return

    # Wrap items in tqdm for progress bar if requested
    if progress:
        items = tqdm(items)

    # Main processing loop
    results = [process_item(item).model_dump() for item in items]

    # Write results to the output file
    with open(output_file, "w") as outfile:
        json.dump(results, outfile, indent=2)
