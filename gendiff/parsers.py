import json
import yaml
import os


def get_extension(file_path):
    return os.path.splitext(file_path)[-1][1:]


def read_data_from_file(file_path, extension):
    if extension == 'yaml' or 'yml':
        with open(file_path) as yaml_file:
            return yaml.load(yaml_file, Loader=yaml.FullLoader)
    elif extension == 'json':
        with open(file_path) as json_file:
            return json.load(json_file)


def get_parsed_data(filepath):
    extension = get_extension(filepath)
    raw_data = read_data_from_file(filepath, extension)
    return raw_data
