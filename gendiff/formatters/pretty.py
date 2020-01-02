from gendiff.constants import NEW, LOST, SAME, CHILDREN, CHANGED, INDENT


def render(data, level=1):
    result = []
    indent = INDENT * level
    for key, description in data.items():
        type_ = description.get('type')
        value = description.get('value')

        if type_ == CHILDREN:
            result.append('{}{} {}: {{'.format(indent, SAME, key))
            result.append(render(value, level + 2))
            result.append('{}}}'.format(indent + INDENT))

        elif type_ == CHANGED:
            new_value = description.get('new_value')
            old_value = description.get('old_value')
            result.append('{}{} {}: {}'.format(indent, NEW, key, new_value))
            result.append('{}{} {}: {}'.format(indent, LOST, key, old_value))

        else:  # for types LOST, SAME, NEW
            result.append('{}{} {}: {}'.format(
                indent, type_, key, get_str_value(value, level)))

    if level == 1:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def get_str_value(value, level=1):
    result = ''

    if isinstance(value, dict):
        if 'type' in value:  # if nested dict
            result += get_str_value(value.get('value'), level + 1)
        else:  # if not nested dict
            result += ('{\n')
            for k, v in value.items():
                result += ('{}{}: {}\n'.format(INDENT * (level + 3), k, v))
                result += ('{}}}'.format(INDENT * (level + 1)))

    else:  # if the value is not dict
        if type(value) is bool:
            result += str(value).lower()
        else:
            result += str(value)

    return result
