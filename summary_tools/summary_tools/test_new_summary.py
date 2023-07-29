from pathlib import Path
from typing import List
import pytest
from summary_tools.filesystem_tools.fs_test_tools import empty_directory
from summary_tools.new_summary import generate_new_summary
from summary_tools.string_tools.string_tools import kebab_case, pascal_case
from summary_tools.ui.cli.cli_test_tools import CLIMock


@pytest.fixture
def summary_template_path() -> Path:
    return Path("")  # Todo


def add_books_to_directory(path: Path, books_names: List[str]) -> Path:
    return path  # Todo


def test_generate_new_summary(empty_directory: Path, summary_template_path: Path):
    CHOOSE_FIRST_BOOK = 0
    CHAPTER_NUMBER = 0
    CHAPTER_NAME = "Chapter Name"
    SUMMARY_WRITER = "Summary Writer"

    FIRST_BOOK = "First Book 2nd Edition by James and Robert"
    SECOND_BOOK = "Second Book"

    directory_with_books = add_books_to_directory(
        empty_directory, [FIRST_BOOK, SECOND_BOOK])
    cli_mock = CLIMock(options_choices=[CHOOSE_FIRST_BOOK], number_inputs_choices=[
                       CHAPTER_NUMBER], string_input_choices=[SUMMARY_WRITER, CHAPTER_NAME])
    generate_new_summary(cli_mock, directory_with_books, summary_template_path)
    assert (directory_with_books / FIRST_BOOK /
            f"{CHAPTER_NUMBER}_{pascal_case(CHAPTER_NAME)}_{kebab_case(SUMMARY_WRITER)}")
