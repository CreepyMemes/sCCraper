import os
import re
import json
from typing import Any


DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")


def clean_filename(title: str) -> str:
    """
    Cleans the title from trash so it can be safely used as a filename.
    """
    return re.sub(r'[^a-zA-Z0-9_-]', '', title.replace(' ', '_'))


def get_data_dir():
    """
    Returns directory path for the output data.
    """
    return os.path.join(DATA_DIR)


def get_challenge_dir(event: str, section: str, title: str) -> str:
    """
    Returns directory path for a challenge.
    """
    return os.path.join(DATA_DIR, 'challenges', clean_filename(event), clean_filename(section), clean_filename(title))


def ensure_dir(path: str):
    """
    Create a directory if it doesn't exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)    


def save_json(file_path: str, data: dict[str, Any]):
    """
    Saves the given dict to a json file in the given path
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
