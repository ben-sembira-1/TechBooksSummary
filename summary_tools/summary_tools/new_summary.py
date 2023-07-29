from pathlib import Path
from sys import stdin, stdout
import sys
from typing import List
from summary_tools.books.books_search import get_all_existing_book_paths
from summary_tools.chapter_summary.chapter_summary_metadata import ChapterSummaryMetadata
from summary_tools.ui.cli.cli import CLI
from summary_tools.ui.ui import UI, Option


# def get_chapter_summary_metadata() -> ChapterSummaryMetadata:
#     # Todo
#     return ChapterSummaryMetadata("writer name", 0, "chapter name")


def choose_book_from_path(ui_provider: UI, path: Path) -> Path:
    all_books_paths = get_all_existing_book_paths(path)
    return ui_provider.choose_from("Books", [Option(name=book_path.name, value=book_path) for book_path in all_books_paths])


def create_new_chapter_summary(metadata: ChapterSummaryMetadata) -> None:
    pass


def main(args: List[str]):
    _, books_directory = args
    cli = CLI(stdin, stdout)
    book_name = choose_book_from_path(cli, Path(books_directory))
    cli.output.write(f"{book_name=}")
    # chapter_summary_metadata = get_chapter_summary_metadata()
    # create_new_chapter_summary(chapter_summary_metadata)


if __name__ == "__main__":
    main(sys.argv)
