from pathlib import Path
import itertools

from summary_tools.filesystem_tools.fs_test_tools import empty_directory
from .books_search import get_all_existing_book_paths


def test_list_directory_books(empty_directory: Path):
    books_directory = empty_directory

    initial_books = ("AUTHORA_bookName", "AUTHORB_SomthingElseEdition2-refactored")
    not_book_names = ("something_else", ".private_things", ".WEIRD_PRIVATE")

    for subdir in itertools.chain(initial_books, not_book_names):
        (books_directory / subdir).mkdir()

    books_found = tuple(book_path.name for book_path in get_all_existing_book_paths(books_directory))
    assert sorted(initial_books) == sorted(books_found)

