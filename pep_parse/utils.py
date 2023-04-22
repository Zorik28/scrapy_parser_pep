import logging
from pathlib import Path


def mkdir_and_path(path: Path, directory: str, filename: str) -> Path:
    """Creats a directory and return the path, and also catches the erorrs."""
    try:
        path_dir = path / directory
        path_dir.mkdir(exist_ok=True)
        return path_dir / filename
    except OSError:
        logging.exception(
            f'Error occurred while creating the folder -> {directory}!',
            stack_info=True
        )
