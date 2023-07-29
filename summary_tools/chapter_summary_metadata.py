from dataclasses import dataclass

@dataclass
class ChapterSummaryMetadata:
    writer: str
    chapter_number: int
    chapter_name: str

    def formatted_representation_no_spaces(self):
        return "" # Todo