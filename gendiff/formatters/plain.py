from gendiff.constants import NEW, LOST, NESTED, CHANGED, COMPLEX, SAME


def render(data, current_path=''):
    if not isinstance(data, dict):
        return str(data)
    result = []
    for property_name, property_description in data.items():
        pathname = update_pathname(current_path, property_name)
        type_ = property_description.get('type')

        # if the property is new
        if type_ == NEW:
            current_value = get_str_value(property_description)
            entry = "Property '{}' was added with value: '{}'".format(
                pathname, current_value)

        # if the property is nested
        elif type_ == NESTED:
            current_value = property_description.get('value')
            entry = render(current_value, pathname)

        # if the property was lost
        elif type_ == LOST:
            entry = "Property '{}' was removed".format(pathname)

        # if the value of property was changed
        elif type_ == CHANGED:
            old_value = property_description.get('old_value')
            new_value = property_description.get('new_value')
            entry = "Property '{}' was changed. From '{}' to '{}'".format(
                pathname, old_value, new_value)

        # if the value stays the same
        elif type_ == SAME:
            continue

        result.append(entry)
    return '\n'.join(result).strip()


def get_str_value(property_description):
    value = property_description.get('value')
    if isinstance(value, dict):
        return COMPLEX
    else:
        return str(value)


def update_pathname(current_path, property_name):
    if not current_path:
        current_path = property_name
    else:
        current_path = '{}.{}'.format(current_path, property_name)
    return current_path
