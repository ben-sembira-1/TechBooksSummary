from functools import reduce

STANDARD_SEPARATORS = (" ", "_", "-", ".")

def multi_replace(string: str, old: tuple[str], new: str) -> list[str]:
    if len(old) == 0:
        raise ValueError("old should include at least one string.")

    return reduce(
        lambda replaced_string, to_replace: replaced_string.replace(to_replace, new),
        old,
        string
    )

def pascalcase(string: str) -> str:
    only_spaces = multi_replace(string, old=STANDARD_SEPARATORS, new=" ")
    return "".join(only_spaces.title().split(" "))

def kebabcase(string: str) -> str:
    only_spaces = multi_replace(string, old=STANDARD_SEPARATORS, new=" ")
    return "-".join(only_spaces.lower().split(" "))