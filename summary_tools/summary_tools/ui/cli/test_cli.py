import re
from typing import List
import pytest
from summary_tools.ui.ui import Option
from .cli import CLI, CLIError
from .cli_test_tools import InputMock, OutputMock


@pytest.fixture
def ten_options_of_multiples_of_5() -> List[Option[int]]:
    return [Option(f"option {idx}", idx * 5) for idx in range(10)]


@pytest.mark.parametrize("option_chosen", [0, 3, 9])
def test_cli_choose_from_valid_input(ten_options_of_multiples_of_5: List[Option[int]], option_chosen: int):
    input = InputMock([f'{option_chosen}'])
    output = OutputMock()

    cli = CLI(input, output)

    assert cli.choose_from(
        "test options", ten_options_of_multiples_of_5) == option_chosen * 5


def test_cli_choose_from_not_a_number(ten_options_of_multiples_of_5: List[Option]):
    input = InputMock(['abc'])
    output = OutputMock()

    cli = CLI(input, output)

    with pytest.raises(CLIError):
        cli.choose_from("test options", ten_options_of_multiples_of_5)


@pytest.mark.parametrize("index_to_check", [-1, 10])
def test_cli_choose_from_out_of_range(ten_options_of_multiples_of_5: List[Option], index_to_check):
    input = InputMock([f'{index_to_check}'])
    output = OutputMock()

    cli = CLI(input, output)

    with pytest.raises(CLIError, match=re.compile("out of range")):
        cli.choose_from("test options", ten_options_of_multiples_of_5)


@pytest.mark.parametrize("number", [-1, 3, 99999999999999999999999999999999])
def test_cli_get_number_valid_number(number):
    INSTRUCTIONS = "instructions"

    input = InputMock([f'{number}'])
    output = OutputMock()
    cli = CLI(input, output)

    assert cli.get_integer(INSTRUCTIONS) == number


@pytest.mark.parametrize("number", ["abc", "", 0.3, 1e3])
def test_cli_get_integer_invalid_integer(number):
    INSTRUCTIONS = "instructions"

    input = InputMock([f'{number}'])
    output = OutputMock()
    cli = CLI(input, output)

    with pytest.raises(CLIError, match=re.compile("Expected an integer")):
        cli.get_integer(INSTRUCTIONS) == number
