from dataclasses import dataclass

from summary_tools.string_tools.string_tools import kebab_case, pascal_case


@dataclass
class ChapterSummaryMetadata:
    writer: str
    chapter_number: int
    chapter_name: str

    def repr_no_spaces(self):

        return f"{self.chapter_number}_{pascal_case(self.chapter_name)}__{kebab_case(self.writer)}"
