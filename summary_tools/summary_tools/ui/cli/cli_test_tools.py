from typing import Iterable


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
