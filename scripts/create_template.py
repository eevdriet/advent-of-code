#!/usr/bin/env python3

import json
import sys
from pathlib import Path

from templater.create import create_file

ROOT_PATH = Path(__file__).parent.parent
DATA_PATH = ROOT_PATH / "data"
TEMPLATE_PATH = ROOT_PATH / "templates"


def create_py_files(patterns: dict):
    stem = "{{padded_day}}_{{uslug}}"

    sources = [TEMPLATE_PATH / "problem.py", TEMPLATE_PATH / "test.py"]
    destinations = [
        ROOT_PATH / "python" / "src" / f'_{patterns["year"]}' / f"day_{stem}",
        ROOT_PATH / "python" / "test" / f"_{patterns["year"]}" / f"test_{stem}",
    ]

    for src, dst in zip(sources, destinations):
        create_file(src, dst.with_suffix(".py"), patterns)


TEMPLATE_CREATORS = {"python": create_py_files}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_template.py <day> <year> [<language>]")
        sys.exit(1)

    day, year, language = sys.argv[1:4]

    if language not in TEMPLATE_CREATORS:
        print(f"No template defined for {language}")
        sys.exit(1)

    info_path = DATA_PATH / f"{year}" / f"{day}.json"
    if not info_path.exists():
        print(f"Path with problem information {info_path} doesn't exist")
        sys.exit(1)

    with open(info_path, "r") as file:
        info = json.load(file)

    creator = TEMPLATE_CREATORS[language]
    creator(info)
