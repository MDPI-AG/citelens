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

from pathlib import Path
from typing import Annotated

from typer import Argument, Typer

app = Typer()


@app.command()
def citelens(
    input_file: Annotated[Path, Argument(help="Path to the input file containing citation information.")],
    output_file: Annotated[Path, Argument(help="Path to the output file")] = "-",
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
    print(f"Processing input file: {input_file}")
    print(f"Results will be saved to: {output_file}")
