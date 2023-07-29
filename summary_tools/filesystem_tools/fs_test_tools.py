from pathlib import Path
import tempfile
from typing import Iterator
import pytest


@pytest.fixture
def empty_directory() -> Iterator[Path]:
    with tempfile.TemporaryDirectory() as directory:
        yield Path(directory)
