import json
import yaml
import os


def get_extension(file_path):
    return os.path.splitext(file_path)[-1][1:]


def read_data_from_file(file_path, extension):
    if extension == 'yaml' or 'yml':
        return yaml.load(open(file_path), Loader=yaml.FullLoader)
    elif extension == 'json':
        return json.load(open(file_path))


def get_parsed_data(filepath):
    extension = get_extension(filepath)
    raw_data = read_data_from_file(filepath, extension)
    return raw_data
