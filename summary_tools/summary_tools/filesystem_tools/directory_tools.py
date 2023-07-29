from pathlib import Path
from typing import Iterator

def subdirectories(path: Path) -> Iterator[Path]:
    for child in path.iterdir():
        if child.is_dir():
            yield child