import json
import os
import re
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from html2text import HTML2Text

# Load session token and setup request headers
ROOT_PATH = Path(__file__).parent.parent
DATA_PATH = ROOT_PATH / "data"
load_dotenv(dotenv_path=ROOT_PATH / ".env")

SESSION = os.getenv("AOC_SESSION")
HEADERS = {"Cookie": f"session={SESSION}", "User-Agent": "github.com/eevdriet"}


class MarkdownConverter(HTML2Text):
    def __init__(self):
        super().__init__()
        self.body_width: int = 0
        self.ignore_links: bool = False
        self.backquote_code_style: bool = True


def fetch_input(year: int, day: int):
    # Fetch the input text
    URL = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    # If valid, save to the correct file
    padded_day = f"{day:02}"

    with open(
        DATA_PATH / f"{year}" / f"{padded_day}.input", "w", encoding="utf-8"
    ) as file:
        file.write(response.text.strip())


def fetch_problem(year: int, day: int, fetch_part2: bool = True):
    # Fetch the problem statement
    URL = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    # Retrieve the soup and determine the problem text and title
    soup = BeautifulSoup(response.text, "html.parser")

    parts = soup.find_all("article", class_="day-desc")
    if not parts:
        return

    part1 = parts[0]
    part2 = parts[1] if len(parts) >= 2 and fetch_part2 else None

    # Extract the problem title from the <h2> title element
    title = part1.find("h2").get_text(strip=True)
    if not (match := re.match(r".*: (.*) ---", title)):
        return

    def extract_text(part) -> str:
        if not part:
            return ""

        part.find("h2").decompose()

        # Convert HTML problem statement to valid Markdown
        converter = MarkdownConverter()
        text: str = converter.handle(str(part))
        text = text.replace("\n\n\n", "\n\n")

        # Split very long lines on line endings and add the endings
        lines = re.split(r"([\.!?] )", text)
        for idx in range(1, len(lines), 2):
            lines[idx] = f"{lines[idx].strip()}\n"

        return "".join((line for line in lines if not line.isspace())).strip()

    # Return the problem information as a JSON
    info = {"description": ""}

    info["title"] = match[1]
    info["clean_title"] = re.sub(r'[/\'".?!]', "", info["title"])
    info["slug"] = re.sub(r"(?:\s|,)+", "-", info["clean_title"].lower())
    info["uslug"] = info["slug"].replace("-", "_")

    return json.dumps(
        {
            **info,
            "day": day,
            "padded_day": f"{day:02}",
            "year": year,
            "url": URL,
            "part1": extract_text(part1),
            "part2": extract_text(part2),
        },
        indent=4,
    )


def main():
    import argparse

    today = date.today()

    # Parse day and year arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, default=today.day)
    parser.add_argument("--year", type=int, default=today.year)
    parser.add_argument("--part-2", type=bool, default=True)
    args = parser.parse_args()

    # Retrieve input and example files for the given problem
    fetch_input(args.year, args.day)

    print(fetch_problem(args.year, args.day))


if __name__ == "__main__":
    main()
