from pathlib import Path
from typing import List
import mimetypes
import sys

def is_text_file(filepath: str) -> bool:
    """
    Return True if filepath has a .txt extension (case-insensitive), otherwise False.
    """
    path = Path(filepath)
    return path.suffix.lower() == ".txt"


def general_error_free(filepath: str) -> bool:
    path = Path(filepath)
    if not path.exists():
        print(f"File not found: {filepath}")
        return False

    if not is_text_file(filepath):
        ext = path.suffix.lower()
        mime = mimetypes.guess_type(filepath)[0]
        actual = mime if mime else (ext if ext else "no extension")
        print(f"Actual file type: '{actual}'. Please choose a .txt file.")
        return False
    return True


def keywords_load(filepath: str) -> List[str]:
    """
    If filepath is a .txt file, read it and return a list where each element is a line (without trailing newline).
    If not a .txt file, print the actual file type and advise selecting a .txt file, then return an empty list.
    """
    path = Path(filepath)
    
    if not general_error_free(filepath):
        return []

    try:
        with path.open("r", encoding="utf-8") as f:
            return [line.rstrip("\r\n") for line in f]
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
def reps_load(filepath: str) -> int:
    path = Path(filepath)
    
    if not general_error_free(filepath):
        return []

    try:
        with path.open("r", encoding="utf-8") as f:
            first_line = f.readline()
        first_line = first_line.strip()
        return int(first_line)
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
