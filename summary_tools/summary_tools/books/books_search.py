from typing import Iterator
from pathlib import Path

import re

from summary_tools.filesystem_tools.directory_tools import subdirectories

def book_directory_name_regex() -> re.Pattern:
    START = "^"
    CAPS_ONLY = "[A-Z]+"
    NOT_NOTHING_NO_UNDERSCORES = "[^_]+"
    END = "$"

    book_regular_expression = \
        f"{START}"\
        f"{CAPS_ONLY}"\
        f"_"\
        f"{NOT_NOTHING_NO_UNDERSCORES}"\
        f"{END}"

    return re.compile(book_regular_expression)

def directory_is_a_book(directory_name: Path) -> bool:
    NO_MATCH = None

    book_regex = book_directory_name_regex()
    return book_regex.fullmatch(directory_name.name) is not NO_MATCH

def get_all_existing_book_paths(path: Path) -> Iterator[Path]:
    for directory in subdirectories(path):
        if directory_is_a_book(directory):
            yield directory

