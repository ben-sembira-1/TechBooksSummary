from .string_tools import STANDARD_SEPARATORS, multi_replace, pascalcase, kebabcase

def test_multi_replace():
    assert multi_replace("a b_c-d.e", old=STANDARD_SEPARATORS, new=" ") == "a b c d e"

def test_pascalcase():
    assert pascalcase("one Two THREE f_our") == "OneTwoThreeFOur"

def test_kebabcase():
    assert kebabcase("one Two THREE f_our") == "one-two-three-f-our"
