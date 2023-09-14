import re
from typing import List
import pytest
from summary_tools.ui.ui import Option
from .cli import CLIError
from .cli_test_tools import InputMock, OutputMock, create_test_cli


@pytest.fixture
def ten_options_of_multiples_of_5() -> List[Option[int]]:
    return [Option(f"option {idx}", idx * 5) for idx in range(10)]


@pytest.mark.parametrize("option_chosen", [0, 3, 9])
def test_cli_choose_from_valid_input(ten_options_of_multiples_of_5: List[Option[int]], option_chosen: int):
    cli = create_test_cli(input=InputMock([f'{option_chosen}']))

    assert cli.choose_from(
        "test options", ten_options_of_multiples_of_5) == option_chosen * 5


def test_cli_choose_from_not_a_number(ten_options_of_multiples_of_5: List[Option]):
    cli = create_test_cli(input=InputMock(['abc']))

    with pytest.raises(CLIError):
        cli.choose_from("test options", ten_options_of_multiples_of_5)


@pytest.mark.parametrize("index_to_check", [-1, 10])
def test_cli_choose_from_out_of_range(ten_options_of_multiples_of_5: List[Option], index_to_check):
    cli = create_test_cli(input=InputMock([f'{index_to_check}']))

    with pytest.raises(CLIError, match=re.compile("out of range")):
        cli.choose_from("test options", ten_options_of_multiples_of_5)


@pytest.mark.parametrize("number", [-1, 3, 99999999999999999999999999999999])
def test_cli_get_number_valid_number(number):
    INSTRUCTIONS = "instructions"

    cli = create_test_cli(input=InputMock([f'{number}']))

    assert cli.get_integer(INSTRUCTIONS) == number


@pytest.mark.parametrize("number", ["abc", 0.3, 1e3])
def test_cli_get_integer_invalid_integer(number):
    INSTRUCTIONS = "instructions"

    cli = create_test_cli(input=InputMock([f'{number}']))

    with pytest.raises(CLIError, match=re.compile(r"Expected an integer")):
        cli.get_integer(INSTRUCTIONS)


def test_cli_empty_input():
    INSTRUCTIONS = "instructions"
    cli = create_test_cli(input=InputMock(["", ""]))

    with pytest.raises(CLIError, match=re.compile(r"[Ee]mpty .* not allowed")):
        cli.get_integer(INSTRUCTIONS)


def test_cli_output():
    MESSAGE = " multi\nline\nmessage "
    NO_RE_MATCH = None

    output_mock = OutputMock()
    error_output_mock = OutputMock()
    cli = create_test_cli(output=output_mock, error_output=error_output_mock)
    cli.show_info_message(MESSAGE)
    assert re.fullmatch(f"-+\n{MESSAGE}\n", output_mock.output) != NO_RE_MATCH
    assert error_output_mock.output == ""


def test_cli_error():
    MESSAGE = " multi\nline\nmessage "
    NO_RE_MATCH = None
    FAILURE_COLOR = r'\033\[91m'

    error_output_mock = OutputMock()
    output_mock = OutputMock()
    cli = create_test_cli(output=output_mock, error_output=error_output_mock)
    cli.show_error_message(MESSAGE)
    assert re.fullmatch(f"-+\n", output_mock.output)
    assert re.fullmatch(f"{FAILURE_COLOR}{MESSAGE}\n",
                        error_output_mock.output) != NO_RE_MATCH
