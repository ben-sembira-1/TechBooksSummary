from pathlib import Path
import pytest
from summary_tools.filesystem_tools.fs_test_tools import empty_directory


@pytest.fixture
def summary_template_path(empty_directory: Path) -> Path:
    local_template_path = Path(__file__).parent / ".template.md"
    assert local_template_path.exists()
    template_path = (empty_directory / ".template.md")
    template_path.write_bytes(local_template_path.read_bytes())
    return template_path
