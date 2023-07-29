from dataclasses import dataclass

from summary_tools.string_tools.string_tools import kebabcase, pascalcase

@dataclass
class ChapterSummaryMetadata:
    writer: str
    chapter_number: int
    chapter_name: str

    def repr_no_spaces(self):
        
        return f"{self.chapter_number}_{pascalcase(self.chapter_name)}__{kebabcase(self.writer)}"