from pathlib import Path

from summary_tools.chapters.chapter_summary_metadata.chapter_summary_metadata import ChapterSummaryMetadata
from summary_tools.ui import ui


def get_chapter_summary_metadata(ui_provider: ui.UI) -> ChapterSummaryMetadata:
    # Todo
    return ChapterSummaryMetadata("writer name", 3, "chapter name")


def create_new_chapter_summary(ui_provider: ui.UI, book_path: Path, template_path: Path):
    summary_metadata = get_chapter_summary_metadata(ui_provider)
