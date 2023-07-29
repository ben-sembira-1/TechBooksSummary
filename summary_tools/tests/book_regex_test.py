import pytest

from ..new_summary import book_directory_name_regex

@pytest.mark.parametrize("directory_name",[
    "A_a",
    "A_A",
    "ABC_aAbB",
    "ABC_AaAa",
    "A1_aA1Aa",
])
def test_book_directory_name_regex_valid_names(directory_name):
    assert book_directory_name_regex().fullmatch(directory_name) is not None


@pytest.mark.parametrize("directory_name",[
    "_a",
    "A_",
    "Aa",
    "a_a",
    "AaA_a",
])
def test_book_directory_name_regex_invalid_names(directory_name):
    assert book_directory_name_regex().fullmatch(directory_name) is None