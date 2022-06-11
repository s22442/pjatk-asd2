import os
import sys


def create_path_without_extension(path: str):
    return os.path.splitext(path)[0]


def read_from(path: str):
    try:
        f = open(path, "r")
    except OSError:
        sys.exit(f"Could not open the file: {path}")

    content = f.read()
    f.close()

    return content


def write_to(path: str, content: str):
    f = open(path, "w")
    f.write(content)
    f.close()
    print(f"Written to {path}")


def write_dict_as_yaml_to(path: str, dictionary: dict):
    yaml = ""
    for k, v in dictionary.items():
        yaml += f"'{k}': {v}\n"

    write_to(path, yaml)
