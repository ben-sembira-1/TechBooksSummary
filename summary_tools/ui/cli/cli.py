
from dataclasses import dataclass
from typing import Iterator, List, Protocol, Generic, TypeVar

from summary_tools.ui import ui

OptionType = TypeVar("OptionType")


def choose_from_options_no_negative_index(options: List[OptionType], index: int):
    if index < 0 or index >= len(options):
        raise CLIError(
            f"The option specified is out of range. got {index}, but range is 0-{len(options) - 1}"
        )
    return options[index]


class Input(Protocol):
    def read(self) -> str:
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

        self.output.write(
            f"From these {options_set_name}, choose the number that represents your choice:\n\n")
        for index, option in enumerate(options):
            self.output.write(f"({index}) - {option.name}\n")
        self.output.write("\n>>>")
        chosen_option = self.input.read()
        self.output.write("\n")

        try:
            return choose_from_options_no_negative_index(options, int(chosen_option)).value
        except ValueError as e:
            raise CLIError(
                f"Expected a number, got: \"{chosen_option}\" instead"
            ) from e
