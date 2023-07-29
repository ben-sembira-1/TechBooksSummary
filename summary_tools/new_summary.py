from pathlib import Path
from summary_tools.books.books_search import get_all_existing_book_paths
from summary_tools.chapter_summary_metadata import ChapterSummaryMetadata

def get_chapter_summary_metadata() -> ChapterSummaryMetadata:
    # Todo
    return ChapterSummaryMetadata("writer name", 0, "chapter name")

def get_book_name() -> str:
    all_book_names = get_all_existing_book_paths(Path("."))
    # chosen_book_name = let_user_choose_book(all_book_names)

def create_new_chapter_summary(metadata: ChapterSummaryMetadata) -> None:
    pass

def main():
    book_name = get_book_name()
    chapter_summary_metadata = get_chapter_summary_metadata()
    create_new_chapter_summary(chapter_summary_metadata)


if __name__ =="__main__":
    main()