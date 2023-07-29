from typing import Iterator
from dataclasses import dataclass
from pathlib import Path

import re

@dataclass
class ChapterSummaryMetadata:
    writer: str
    chapter_number: int
    chapter_name: str

    def formatted_representation_no_spaces(self):
        return "" # Todo

def get_chapter_summary_metadata() -> ChapterSummaryMetadata:
    # Todo
    return ChapterSummaryMetadata("writer name", 0, "chapter name")

def subdirectories(path: Path) -> Iterator[Path]:
    for child in path.iterdir:
        if child.is_dir():
            yield child

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

def directory_is_a_book(directory_name: str) -> bool:
    NO_MATCH = None

    book_regex = book_directory_name_regex()
    return book_regex.fullmatch(directory_name) is not NO_MATCH

def get_all_existing_book_paths() -> Iterator[Path]:
    for directory in subdirectories(Path(".")):
        if directory_is_a_book(directory):
            yield directory

def get_book_name() -> str:
    all_book_names = get_all_existing_book_names()
    chosen_book_name = let_user_choose_book(all_book_names)

def create_new_chapter_summary(metadata: ChapterSummaryMetadata) -> None:
    pass

def main():
    book_name = get_book_name()
    chapter_summary_metadata = get_chapter_summary_metadata()
    create_new_chapter_summary(chapter_summary_metadata)


if __name__ =="__main__":
    main()