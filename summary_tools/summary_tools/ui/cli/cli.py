
from dataclasses import dataclass
from typing import List, Protocol, TypeVar

from summary_tools.ui import ui

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
    input: Input
    output: Output

    def choose_from(self, options_set_name: str, options: List[ui.Option[T]]) -> T:
        assert len(
            options) > 0, "At least one option to choose from should be given."

        self._draw_buffer()
        self.output.write(
            f"From these {options_set_name}, choose the number that represents your choice:\n\n")
        for index, option in enumerate(options):
            self.output.write(f"({index}) - {option.name}\n")
        chosen_option = self.get_integer()

        return choose_from_options_no_negative_index(options, int(chosen_option)).value

    def show_message(self, message: str):
        self._draw_buffer()
        self.output.write(message + "\n")

    def get_integer(self, instructions: str | None = None) -> int:
        input_got = self._detailed_read_input(instructions, "number")
        try:
            number = int(input_got)
        except ValueError as e:
            raise CLIError(
                f"Expected an integer, got: \"{input_got}\" instead"
            ) from e

        return number

    def get_string(self, instructions: str | None = None) -> str:
        return self._detailed_read_input(instructions, "string")

    def _detailed_read_input(self, instructions: str | None, hint: str) -> str:
        self._draw_buffer()
        if instructions is not None:
            self.output.write(f"{instructions}\n")

        return self._read_input(hint)

    def _read_input(self, hint: str) -> str:
        self.output.write(f"\n({hint}) >>> ")
        chosen_option = self.input.readline()
        self.output.write("\n")
        return chosen_option

    def _draw_buffer(self):
        self.output.write("---------------------------------------")
