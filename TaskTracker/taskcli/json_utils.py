import json
from typing import Literal, TypedDict
import os

Status = Literal["todo", "in_progress", "done"]
file_path = "todo_file.json"


class JsonTaskDict(TypedDict):
    id: int
    title: str
    Status: Status


class JsonFileStructureDict(TypedDict):
    tasks: list[JsonTaskDict]


def init_json_file(file_path: str = file_path) -> None:
    if not os.path.exists(file_path):
        initial_data: JsonFileStructureDict = {"tasks": []}
        write_json_file(initial_data, file_path=file_path)


def read_json_file(file_path: str = file_path) -> JsonFileStructureDict:
    with open(file_path, "r") as file:
        data: JsonFileStructureDict = json.load(file)
    return data


def write_json_file(data: JsonFileStructureDict, file_path: str = file_path) -> bool:
    try:
        json_data = json.dumps(data, indent=2)
        with open(file_path, "w") as file:
            file.write(json_data)
        return True
    except Exception:
        return False
