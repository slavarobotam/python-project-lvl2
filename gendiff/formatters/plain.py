INDENT = '  '
NEW, LOST, SAME = '+', '-', ' '
CHILDREN = 'children'
CHANGED = 'changed'
COMPLEX = 'complex value'


def render(data, gpath=''):
    if type(data) != dict:
        return str(data)
    result = []
    for key in data:
        if not gpath:
            path = key
        else:
            path = '{}.{}'.format(gpath, key)
        if data[key]['type'] == NEW and 'type' not in data[key]:
            result.append("Property '{}' was added with value: '{}'".format(key, COMPLEX))  # noqa E501
        elif data[key]['type'] == NEW and 'type' in data[key]:
            result.append("Property '{}' was added with value: '{}'".format(
                path, get_val(data[key]['value'])))
        elif data[key]['type'] == CHILDREN and type(data[key]['value']) == dict:  # noqa E501
            result.append(render(data[key]['value'], path))
        elif data[key]['type'] == LOST:
            result.append("Property '{}' was removed".format(path))
        elif data[key]['type'] == CHANGED:
            result.append("Property '{}' was changed. From '{}' to '{}'".format(  # noqa E501
                path, get_val(data[key]['old_value']), get_val(data[key]['new_value'])))  # noqa E501
    return '\n'.join(result).strip()


def get_val(value):
    if type(value) == dict:
        return COMPLEX
    else:
        return str(value)
