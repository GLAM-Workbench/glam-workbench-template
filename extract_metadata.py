import json
from pathlib import Path
from typing import Any, Dict

INPUT_FILE = "cookiecutter.json"
OUTPUT_FILE = "metadata.json"
FIELDS = {
    "project_name",
    "project_description",
    "creators",
}


def main():
    metadata = extract_metadata(INPUT_FILE)
    with open(OUTPUT_FILE, "w") as output_file:
        output_file.write(json.dumps(metadata))


def extract_metadata(file: Path) -> Dict[str, Any]:
    with open(file) as info:
        data: Dict[str, Any] = json.load(info)
        result = {k: v for (k, v) in data.items() if k in FIELDS}
    return result


if __name__ == "__main__":
    main()
