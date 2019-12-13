INDENT = '  '
NEW, LOST, SAME = '+', '-', ' '
CHILDREN = 'children'
CHANGED = 'changed'
COMPLEX = 'complex value'


def render(data, level=1):
    if type(data) != dict:
        return str(data)
    result = []
    indent = INDENT * level
    if level == 1:
        result.append('{')
    for key in data:
        if data[key]['type'] == CHILDREN:
            result.append('{}{} {}: {{'.format(indent, SAME, key))
            result.append(render(data[key]['value'], level + 2))
            result.append('{}}}'.format(indent + INDENT))
        elif data[key]['type'] == CHANGED:
            result.append('{}{} {}: {}'.format(
                indent, NEW, key, data[key]['new_value']))
            result.append('{}{} {}: {}'.format(
                indent, LOST, key, data[key]['old_value']))
        else:
            result.append('{}{} {}: {}'.format(
                indent, data[key]['type'], key, get_value(data[key], level)))
    if level == 1:
        result.append('}')
    return '\n'.join(result)


def get_value(value, level=1):
    res = ''
    if isinstance(value, dict) and 'type' not in value:
        res += ('{\n')
        for k, v in value.items():
            res += ('{}{}: {}\n'.format(INDENT * (level + 2), k, v))
            res += ('{}}}'.format(INDENT * level))
    elif isinstance(value, dict) and 'type' in value:
        res = get_value(value['value'], level + 1)
    else:
        if type(value) is bool:
            res = str(value).lower()
        else:
            res = str(value)
    return res


def render_plain(data, path=''):
    if type(data) != dict:
        return str(data)
    result = []
    for key in data:
        if not path:
            path = key
        else:
            path = '{}.{}'.format(path, key)
        if type(data[key]) == dict and 'type' not in data[key]:
            result.append('Property {} was added with value: {}'.format(key, COMPLEX))  # noqa E501
        if data[key]['type'] == NEW:
            result.append('Property {} was added with value: {}'.format(
                path, data[key]['value']))
        elif data[key]['type'] == SAME and type(data[key]['value']) == dict:
            result.append(render_plain(data[key]['value'], path))
        elif data[key]['type'] == LOST:
            result.append('Property {} was removed'.format(key))
        elif data[key]['type'] == CHANGED:
            result.append('Property {} was changed. From {} to {}'.format(
                key, data[key]['old_value'], data[key]['new_value']))
        else:
            result.append('OOOOOOOOOOOOO')
    return '\n'.join(result)
