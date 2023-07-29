from pathlib import Path
from summary_tools.chapters.chapter_summary_metadata.chapter_summary_metadata import ChapterSummaryMetadata
from summary_tools.chapters.chapters import create_new_chapter_summary, get_chapter_summary_metadata
from summary_tools.chapters.chapters_test_tools import summary_template_path
from summary_tools.filesystem_tools.fs_test_tools import empty_directory
from summary_tools.string_tools.string_tools import kebab_case, pascal_case
from summary_tools.ui.cli.cli_test_tools import CLIMock


def test_create_new_chapter_summary(empty_directory: Path, summary_template_path: Path):
    CHAPTER_NUMBER = 0
    CHAPTER_NAME = "Chapter Name"
    SUMMARY_WRITER = "Summary Writer"

    cli_mock = CLIMock(options_choices=[], integer_inputs_choices=[
                       CHAPTER_NUMBER], string_input_choices=[SUMMARY_WRITER, CHAPTER_NAME])
    create_new_chapter_summary(
        cli_mock, empty_directory, summary_template_path)

    expected_new_summary_path = (empty_directory /
                                 f"{CHAPTER_NUMBER}_{pascal_case(CHAPTER_NAME)}_{kebab_case(SUMMARY_WRITER)}")
    assert expected_new_summary_path.exists()
    assert expected_new_summary_path.is_file()


def test_get_chapter_summary_metadata():
    CHAPTER_NUMBER = 0
    CHAPTER_NAME = "Chapter Name"
    SUMMARY_WRITER = "Summary Writer"

    cli_mock = CLIMock(options_choices=[], integer_inputs_choices=[
                       CHAPTER_NUMBER], string_input_choices=[SUMMARY_WRITER, CHAPTER_NAME])

    assert get_chapter_summary_metadata(cli_mock) == ChapterSummaryMetadata(
        SUMMARY_WRITER, CHAPTER_NUMBER, CHAPTER_NAME)
    assert cli_mock.messages_shown == [
        "What is your name?", "What chapter are you reading?", "What is the name of the chapter?"]
