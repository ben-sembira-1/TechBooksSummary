import pytest

from .chapter_summary_metadata import ChapterSummaryMetadata

def test_chapter_summary_metadata_formatting():
    chapter_summary_metadata = ChapterSummaryMetadata(
        writer="Ben Sembira",
        chapter_number=3,
        chapter_name="Refactoring classes"
    )

    assert chapter_summary_metadata.repr_no_spaces() == "3_RefactoringClasses__ben-sembira"