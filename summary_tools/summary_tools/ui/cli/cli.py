
from sys import stdin, stdout, stderr
from dataclasses import dataclass, field
from typing import List, Protocol, TypeVar

from summary_tools.ui import ui
from summary_tools.ui.cli.colors import Color

OptionType = TypeVar("OptionType")


def choose_from_options_no_negative_index(options: List[OptionType], index: int):
    if index < 0 or index >= len(options):
        raise CLIError(
            f"The option specified is out of range. got {index}, but range is 0-{len(options) - 1}"
        )
    return options[index]


class Input(Protocol):
    def readline(self) -> str:
        ...


class Output(Protocol):
    def write(self, data: str):
        ...


class CLIError(Exception):
    pass


T = TypeVar("T")


@dataclass
class CLI(ui.UI):
    input: Input = stdin
    output: Output = stdout
    error_output: Output = stderr

    def __post_init__(self):
        if self.error_output is None:
            self.error_output = self.output

    def choose_from(self, options_set_name: str, options: List[ui.Option[T]]) -> T:
        assert len(
            options) > 0, "At least one option to choose from should be given."

        self._draw_buffer()
        self._print(
            f"From these {options_set_name}, choose the number that represents your choice:", end="\n\n")
        for index, option in enumerate(options):
            self._print(f"({index}) - {option.name}")
        chosen_option = self.get_integer()

        return choose_from_options_no_negative_index(options, int(chosen_option)).value

    def show_info_message(self, message: str):
        self._draw_buffer()
        self._print(message)

    def show_error_message(self, message: str):
        self._draw_buffer()
        self._print(message, color=Color.FAIL, file=self.error_output)

    def get_integer(self, instructions: str | None = None) -> int:
        input_got = self._detailed_read_input(
            instructions, hint="number", allow_empty=False)
        try:
            number = int(input_got)
        except ValueError as e:
            raise CLIError(
                f"Expected an integer, got: \"{input_got}\" instead"
            ) from e

        return number

    def get_string(self, instructions: str | None = None, *, allow_empty: bool = False) -> str:
        return self._detailed_read_input(instructions, hint="string", allow_empty=allow_empty)

    def _detailed_read_input(self, instructions: str | None, *, hint: str, allow_empty: bool) -> str:
        self._draw_buffer()
        if instructions is not None:
            self._print(f"{instructions}")

        return self._read_input(hint, allow_empty=allow_empty)

    def _read_input(self, hint: str, *, allow_empty: bool) -> str:
        self._print(f"\n({hint}) >>> ", end="")
        input_got = self.input.readline().strip()
        self._print()

        if not allow_empty and not input_got.strip():
            raise CLIError("Empty input not allowed.")

        return input_got

    def _draw_buffer(self):
        self._print("---------------------------------------")

    def _print(self, text: str = "", end: str = "\n", color: Color = Color.NATIVE, file: Output | None = None) -> None:
        if file is None:
            file = self.output
        file.write(f"{color.value}{text}{end}")
