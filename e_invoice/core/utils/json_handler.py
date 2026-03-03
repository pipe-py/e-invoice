import json


def load_json(json_file: str, mode: str = "r", encoding: str = "UTF-8") -> dict:
    with open(file=json_file, mode=mode, encoding=encoding) as file:
        return json.load(file)
