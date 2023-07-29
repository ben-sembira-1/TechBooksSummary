from pathlib import Path

from summary_tools.chapters.chapter_summary_metadata.chapter_summary_metadata import ChapterSummaryMetadata
from summary_tools.ui import ui


def get_chapter_summary_metadata(ui_provider: ui.UI) -> ChapterSummaryMetadata:
    writer_name = ui_provider.get_string("What is your name?")
    chapter_number = ui_provider.get_integer("What chapter are you reading?")
    chapter_name = ui_provider.get_string("What is the name of the chapter?")
    return ChapterSummaryMetadata(writer_name, chapter_number, chapter_name)


def create_new_chapter_summary(ui_provider: ui.UI, book_path: Path, template_path: Path):
    summary_metadata = get_chapter_summary_metadata(ui_provider)
