from pathlib import Path
import pytest
import tempfile

from .fs_test_tools import empty_directory
from .directory_tools import subdirectories

def test_subdirectories(empty_directory: Path):
    directory_with_subdirectories = empty_directory

    subdirectories_names = ("a", "b", "c")
    subfiles_names = ("e", "f", "g")

    for subdirectory in subdirectories_names:
        (directory_with_subdirectories / subdirectory).mkdir()

    for subfile in subfiles_names:
        (directory_with_subdirectories / subfile).touch()

    found_subdirectories = tuple(subdir_path.name for subdir_path in subdirectories(directory_with_subdirectories))
    assert sorted(found_subdirectories) == sorted(subdirectories_names)
