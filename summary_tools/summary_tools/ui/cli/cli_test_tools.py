from dataclasses import dataclass, field
from typing import Iterable, List, TypeVar

from summary_tools.ui import ui
from summary_tools.ui.cli.cli import CLI, Input, Output


class InputMock:
    def __init__(self, responses: Iterable[str]):
        self.responses_iterator = iter(responses)

    def readline(self) -> str:
        return f"{next(self.responses_iterator)}\n"


class OutputMock:
    def __init__(self):
        self.output = ""

    def write(self, data: str):
        self.output += data


def create_test_cli(input: Input | None = None, output: Output | None = None, error_output: Output | None = None):
    return CLI(
        input=input or InputMock([]),
        output=output or OutputMock(),
        error_output=error_output or OutputMock(),
    )


T = TypeVar("T")


@dataclass
class CLIMock(ui.UI):
    options_choices: List[int]
    integer_inputs_choices: List[int]
    string_input_choices: List[str]
    messages_shown: List[str] = field(default_factory=list, init=False)
    errors_shown: List[str] = field(default_factory=list, init=False)

    def choose_from(self, options_set_name: str, options: List[ui.Option[T]]) -> T:
        choice = self.options_choices.pop(0)
        return options[choice].value

    def show_info_message(self, message: str):
        self.messages_shown.append(message)

    def show_error_message(self, message: str):
        self.errors_shown.append(message)

    def get_integer(self, instructions: str | None) -> int:
        if instructions is not None:
            self.messages_shown.append(instructions)
        return self.integer_inputs_choices.pop(0)

    def get_string(self, instructions: str | None, *, allow_empty: bool = False) -> str:
        if instructions is not None:
            self.messages_shown.append(instructions)
        return self.string_input_choices.pop(0)
