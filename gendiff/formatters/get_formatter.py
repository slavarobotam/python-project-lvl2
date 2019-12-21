from . import undefined, plain, json


def get_formatter(format):
    if format == 'plain':
        formatter = plain
    elif format == 'json':
        formatter = json
    else:
        formatter = undefined
    return formatter
