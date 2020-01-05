from gendiff.constants import NEW, LOST, SAME, NESTED, CHANGED, INDENT


def render(data, level=1):
    result = []
    indent = INDENT * level
    for key, description in data.items():
        type_ = description.get('type')
        value = description.get('value')

        if type_ == NESTED:
            result.append('{}{} {}: {{'.format(indent, SAME, key))
            result.append(render(value, level + 2))
            result.append('{}}}'.format(indent + INDENT))

        elif type_ == CHANGED:
            new_value = description.get('new_value')
            old_value = description.get('old_value')
            result.append('{}{} {}: {}'.format(indent, NEW, key, new_value))
            result.append('{}{} {}: {}'.format(indent, LOST, key, old_value))

        else:  # for types LOST, SAME, NEW, SIMPLE
            result.append('{}{} {}: {}'.format(
                indent, type_, key, get_str_value(value, level)))

    if level == 1:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def get_str_value(value, level=1):
    if isinstance(value, dict):
        lines = []
        plain_dict = value.get('value')
        lines.append('{')
        for k, v in plain_dict.items():
            lines.append('{}{}: {}'.format(INDENT * (level + 3), k, v))
            lines.append('{}}}'.format(INDENT * (level + 1)))
        result = '\n'.join(lines)
    else:  # if the value is not dict
        if type(value) is bool:
            result = str(value).lower()
        else:
            result = str(value)
    return result
