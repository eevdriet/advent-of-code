#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path

from templater.create import create_file
from templater.props import props_list

VAULT_PATH = Path.home() / "Sandbox"
ROOT_PATH = Path(__file__).parent.parent
DATA_PATH = ROOT_PATH / "data"
TEMPLATE_PATH = ROOT_PATH / "templates"
LANGUAGE_NOTES = {
    "python": "Python",
    "rust": "Rust",
    "js": "Javascript",
    "ts": "Typescript",
}


def add_part2(path: Path, info: dict):
    if not info["part2"]:
        print("No info on part 2...")
        return

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    # Determine whether part 2 is already filled and if not, replace with the problem statement
    pattern = re.compile(r"(?s)(#+ \[Problem.*?#+ Part 2\s*\n\n)")

    def replacer(match):
        return match.group(1) + info["part2"] + "\n\n"

    # Only rewrite the file if a replacement was actually made
    text, has_replaced = pattern.subn(replacer, text, count=1)
    if not has_replaced:
        print("No replacements for part 2")
        return

    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    if len(sys.argv) < 3:
        print("Usage: python create_note.py <day> <year> [<languages>]")
        sys.exit(1)

    day, year = sys.argv[1:3]
    languages = sys.argv[3:]

    # Load information about the problem
    info_path = DATA_PATH / f"{year}" / f"{day}.json"
    if not info_path.exists():
        print(f"Path with problem information {info_path} doesn't exist")
        sys.exit(1)

    with open(info_path, "r") as file:
        info = json.load(file)

    info["aoc_date"] = f"{info["year"]}-12-{info["padded_day"]}"

    # Alias each problem with its index
    info["aliases"] = props_list([info["title"], f"Advent of code {year} #{day}"])

    # Determine which languages have defined templates
    languages = [f"[[{LANGUAGE_NOTES[l]}]]" for l in languages if l in LANGUAGE_NOTES]
    info["language"] = props_list(languages)

    # Determine where to place the note
    src = TEMPLATE_PATH / "note.md"
    dst = (
        VAULT_PATH
        / "Cards"
        / "Calendar"
        / f"{year}-12-{info['padded_day']} (Advent of code) {info['clean_title']}.md"
    )

    # Either create the file as new or try to add part 2 if it isn't added yet
    if not dst.exists():
        create_file(src, dst, info)
    else:
        print(
            f"Note {dst.name} already exists in the vault, trying to add part 2 text..."
        )
        add_part2(dst, info)


if __name__ == "__main__":
    main()
