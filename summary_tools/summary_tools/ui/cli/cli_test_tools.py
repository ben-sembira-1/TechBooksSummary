from dataclasses import dataclass, field
from typing import Iterable, List, TypeVar

from summary_tools.ui import ui


class InputMock:
    def __init__(self, responses: Iterable[str]):
        self.responses_iterator = iter(responses)

    def readline(self) -> str:
        return next(self.responses_iterator)


class OutputMock:
    def __init__(self):
        self.output = ""

    def write(self, data: str):
        self.output += data


T = TypeVar("T")


@dataclass
class CLIMock(ui.UI):
    options_choices: List[int]
    integer_inputs_choices: List[int]
    string_input_choices: List[str]
    messages_shown: List[str] = field(default_factory=list, init=False)

    def choose_from(self, options_set_name: str, options: List[ui.Option[T]]) -> T:
        choice = self.options_choices.pop()
        return options[choice].value

    def show_message(self, message: str):
        self.messages_shown.append(message)

    def get_integer(self, instructions: str | None) -> int:
        if instructions is not None:
            self.messages_shown.append(instructions)
        return self.integer_inputs_choices.pop()

    def get_string(self, instructions: str | None) -> str:
        if instructions is not None:
            self.messages_shown.append(instructions)
        return self.string_input_choices.pop()
