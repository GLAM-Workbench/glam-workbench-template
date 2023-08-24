import json
import datetime
import os
from pathlib import Path
from typing import Any, Dict, List
from rocrate.rocrate import ROCrate
from rocrate.model.person import Person
from rocrate.model.contextentity import ContextEntity

# Load dummy env variables in dev environment
try:
    from dotenv import load_dotenv
except ImportError:
    pass
else:
    load_dotenv()

INPUT_FILE = "cookiecutter.json"

CC_FIELDS = {
    "project_name",
    "project_description",
    "creators",
}

REPOSITORY_URL = f"https://github.com/{os.getenv('GITHUB_REPOSITORY')}"


def main():
    """
    Create a basic RO-Crate metadata file based on values in the cookie cutter config file
    """

    # Get metadata from cookie-cutter config
    metadata = extract_metadata(Path(INPUT_FILE))

    # Make creators a simple un-nested list
    fix_creator_nesting(metadata)

    # Initialise a crate
    crate = ROCrate()

    # Set the crate root object name to the project name
    crate.name = metadata.get("project_name")
    
    # Set the crate root object description to the project description
    crate.description = metadata.get("project_description")
    
    # Add repository link and current date to root crate
    crate.update_jsonld(
        {
            "@id": "./",
            "url": REPOSITORY_URL,
            "version": "0.0.0",
            "datePublished": datetime.datetime.now().strftime("%Y-%m-%d"),
        }
    )

    # Add people records for creators listed in metadata
    authors = create_people(crate, metadata["creators"])
    
    # Add the people as authors
    crate.add(*authors)

    # Add the authors to the crate root
    root = crate.get("./")
    root.append_to("author", authors)

    # Save the crate file in the cwd
    crate.write(".")


def create_people(crate: ROCrate, creators: List[Dict[str, str]]) -> List[Person]:
    """Converts a list of authors to a list of Persons to be embedded within an ROCrate

    Parameters:
        crate: The rocrate in which the authors will be created.
        authors: A list of author information.

    Returns:
        A list of Persons.
    """
    authors = []

    # Loop though list of people
    for creator in creators:

        # If there's no orcid then use name to create an id
        if not creator["orcid"]:
            creator_id = f"#{creator['name'].replace(', ', '_')}"
        
        # Convert orcid to url if necessary
        elif not creator["orcid"].startswith("http"):
            creator_id = f"https://orcid.org/{creator['orcid']}"
        
        # Otherwise just use orcid as the id
        else:
            creator_id = creator["orcid"]

        # Create the Person entity and add to list of authors to return

        authors.append(Person(crate, creator_id, {"name": creator["name"]}))
    return authors


def extract_metadata(file: Path) -> Dict[str, Any]:
    """
    Extract metadata from the cookie cutter config file
    """
    with open(file) as info:
        data: Dict[str, Any] = json.load(info)
        result = {k: v for (k, v) in data.items() if k in CC_FIELDS}
    return result


def fix_creator_nesting(metadata: Dict[str, Any]) -> None:
    """
    Un-nest the creator data (necessary due to limits on cookie cutter config formatting)
    """
    if "creators" in CC_FIELDS:
        metadata["creators"] = metadata["creators"]["creator_list"]


if __name__ == "__main__":
    main()
