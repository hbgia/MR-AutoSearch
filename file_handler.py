from pathlib import Path
from typing import List
import mimetypes

def is_text_file(filepath: str) -> bool:
    """
    Return True if filepath has a .txt extension (case-insensitive), otherwise False.
    """
    return Path(filepath).suffix.lower() == ".txt"


def can_read_file(filepath: str) -> bool:
    """
    Returns False if there is any problem reading file or the file does NOT has .txt extention. Also prints the error to console.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            f.read()
        
        if not is_text_file(filepath):
            ext = Path(filepath).suffix.lower()
            mime = mimetypes.guess_type(filepath)[0]
            actual = mime if mime else (ext if ext else "no extension")
            print(f"[FILE READING ERROR] Actual file type: '{actual}'. Please choose a .txt file.")    
        return True
    
    except Exception as e:
        print(f"[FILE READING ERROR] {e}")
        return False


def keywords_load(filepath: str) -> List[str]:
    """
    If filepath is a .txt file, read it and return a list where each element is a line (without trailing newline).
    If not a .txt file, print the actual file type and advise selecting a .txt file, then return an empty list.
    """
    path = Path(filepath)
    
    if not can_read_file(filepath):
        return []

    try:
        with path.open("r", encoding="utf-8") as f:
            return [line.rstrip("\r\n") for line in f]
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

from datetime import datetime
def logs_search(searched_word: str, filepath: str) -> bool:
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with path.open("a", encoding="utf-8") as f:
            w = searched_word
            f.write(f"[{now}] {w}\n")
        return True
    except Exception as e:
        print(f"[LOG WRITE ERROR] {e}")
        return False