"""Helpers to work with JSON configuration files."""

import json


def load_json(json_file: str, mode: str = "r", encoding: str = "UTF-8") -> dict:
    """Load a JSON file and return its content.

    Args:
        json_file: Path to the JSON file.
        mode: File opening mode, usually ``"r"``.
        encoding: Text encoding used to read the file.

    Returns:
        The JSON content decoded into a dictionary.
    """
    with open(file=json_file, mode=mode, encoding=encoding) as file:
        return json.load(file)
