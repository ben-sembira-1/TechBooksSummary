from pathlib import Path
from typing import List
import pytest
from summary_tools.chapters.chapters_test_tools import summary_template_path
from summary_tools.filesystem_tools.fs_test_tools import empty_directory
from summary_tools.new_summary import generate_new_summary
from summary_tools.ui.cli.cli_test_tools import InputMock, create_test_cli


def add_books_to_directory(path: Path, books_names: List[str]):
    for book_name in books_names:
        (path / book_name).mkdir()


def test_generate_new_summary(empty_directory: Path, summary_template_path: Path):
    CHOOSE_FIRST_BOOK = "0"
    CHAPTER_NUMBER = "0"
    CHAPTER_NAME = "Chapter Name"
    SUMMARY_WRITER = "Summary Writer"

    FIRST_BOOK = "JAMESANDROBERT_FirstBook"
    SECOND_BOOK = "MARTINLOOTERKING_SecondBook"

    directory_with_books = empty_directory
    add_books_to_directory(
        directory_with_books, [FIRST_BOOK, SECOND_BOOK])

    cli_mock = create_test_cli(input=InputMock(
        [CHOOSE_FIRST_BOOK, SUMMARY_WRITER, CHAPTER_NUMBER, CHAPTER_NAME]))
    generate_new_summary(cli_mock, directory_with_books, summary_template_path)

    expected_summary_path = directory_with_books / \
        FIRST_BOOK / "0_ChapterName__summary-writer.md"
    assert expected_summary_path.exists()
    assert expected_summary_path.is_file()
