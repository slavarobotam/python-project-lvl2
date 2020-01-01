from gendiff.formatters import pretty, plain, json


def get_formatter(format):
    if format == 'plain':
        formatter = plain
    elif format == 'json':
        formatter = json
    else:
        formatter = pretty
    return formatter
