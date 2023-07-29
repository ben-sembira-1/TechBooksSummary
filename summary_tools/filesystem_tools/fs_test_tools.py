from pathlib import Path
import tempfile
import pytest


@pytest.fixture
def empty_directory() -> Path:
    with tempfile.TemporaryDirectory() as directory:
        yield Path(directory)