import abc
from dataclasses import dataclass
from typing import Generic, List, TypeVar

T = TypeVar("T")


@dataclass
class Option(Generic[T]):
    name: str
    value: T


class UI(abc.ABC):
    @abc.abstractmethod
    def choose_from(self, options_set_name: str, options: List[Option[T]]) -> T:
        ...

    @abc.abstractmethod
    def show_message(self, message: str):
        ...

    @abc.abstractmethod
    def get_integer(self, instructions: str | None) -> int:
        ...

    @abc.abstractmethod
    def get_string(self, instructions: str | None, *, allow_empty: bool = False) -> str:
        ...
