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
