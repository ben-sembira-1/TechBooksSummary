from pathlib import Path
# TODO: fire does not have a py.typed module in it, so mypy shouts on it. For now, there is a type: ignore in it.
import fire  # type: ignore
from summary_tools.books.books_search import get_all_existing_book_paths
from summary_tools.chapters import chapters
from summary_tools.ui import ui
from summary_tools.ui.cli.cli import CLI
from summary_tools.ui.ui import UI, Option


def choose_book_from_directory(ui_provider: UI, directory: Path) -> Path:
    all_books_paths = get_all_existing_book_paths(directory)
    return ui_provider.choose_from("Books", [Option(name=book_path.name, value=book_path) for book_path in all_books_paths])


def generate_new_summary(ui_provider: ui.UI, books_directory: Path, summary_template_path: Path):
    book_path = choose_book_from_directory(ui_provider, books_directory)
    chapters.create_new_chapter_summary(
        ui_provider, book_path, summary_template_path)


def cli_create_new_summary(books_directory: str, summary_template_path: str, debug: bool = False):
    cli = CLI()
    try:
        generate_new_summary(cli, Path(books_directory),
                             Path(summary_template_path))
    except BaseException as e:
        if debug:
            import traceback
            cli.show_error_message(traceback.format_exc())
        else:
            cli.show_error_message(
                f"Error: {str(e)} (use --debug for more details)")


def main():
    fire.Fire(cli_create_new_summary)


if __name__ == "__main__":
    main()

