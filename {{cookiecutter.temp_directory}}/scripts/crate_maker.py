from pathlib import Path
from typing import List, Optional, Dict
import os
import argparse
from rocrate.rocrate import ROCrate
from rocrate.model.person import Person
from notebook_embedder import write_metadata

NOTEBOOK_EXTENSION = ".ipynb"
DESCRIPTION = """
Embeds rocrate data within every jupyter notebook in the directory, and then
creates a parent rocrate in the same directory.
"""
DEFAULT_CRATE_PROPERTIES = {}
DEFAULT_CRATE_NAME = "ro-crate-metadata.json"
METADATA_KEY = "ro-crate"
TEMP_DIR = "/tmp/crate_hole"


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("dir", type=Path, help="The directory to act on")
    parser.add_argument(
        "-m",
        "--metadata",
        dest="metadata",
        type=Path,
        help="An optional metadata.json file containing some defaults for author information",
    )
    args = parser.parse_args()
    crates = update_notebook_metadata(args.dir, args.metadata)
    link_crates(crates, args.dir)


def update_notebook_metadata(dir: Path, metadata: Optional[Path]) -> List[ROCrate]:
    """Creates and embeds rocrates in the metadata of all jupyter notebooks in the supplied
    file.

    Parameters:
        dir: The directory in which to act.
        metadata: A metadata file containing author information

    Returns:
        The embedded rocrates.
    """
    notebooks = get_notebooks(dir)
    crates = [generate_rocrate(notebook, metadata) for notebook in notebooks]

    # Embed rocrates
    for notebook, crate in zip(notebooks, crates):
        # Dumb workaround - write crate to temp folder
        temp_dir = Path(TEMP_DIR)
        temp_dir.mkdir(parents=True, exist_ok=True)

        crate.write(temp_dir)
        crate_file = temp_dir.joinpath(DEFAULT_CRATE_NAME)

        with open(crate_file) as in_file:
            data = in_file.read()

        write_metadata(notebook, METADATA_KEY, data)

    return crates


def get_notebooks(dir: Path) -> List[Path]:
    files = [Path(file) for file in os.listdir(dir)]
    is_notebook = lambda file: file.suffix == NOTEBOOK_EXTENSION
    return list(filter(is_notebook, files))


def generate_rocrate(notebook: Path, metadata: Optional[Path]) -> ROCrate:
    crate = ROCrate()
    file = crate.add_file(notebook, properties=extract_properties(notebook, metadata))
    # Add the authors
    authors = extract_authors(crate, notebook, metadata)
    file["author"] = authors
    return crate


def extract_properties(notebook: Path, metadata: Optional[Path]) -> Dict[str, str]:
    return {"name": notebook.name, "encodingFormat": "application/x-ipynb+json"}


def extract_authors(
    crate: ROCrate, notebook: Path, metadata: Optional[Path]
) -> List[Person]:
    orcid = "https://orcid.org/0000-0000-0000-0000"

    return [
        Person(
            crate, orcid, {"name": "Alice Doe", "affiliation": "University of Flatland"}
        )
    ]


def link_crates(crates: List[ROCrate], output_dir: Path) -> None:
    ...


if __name__ == "__main__":
    main()
