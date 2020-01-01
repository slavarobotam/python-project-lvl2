from gendiff.constants import NEW, LOST, CHILDREN, CHANGED, COMPLEX


def render(data, current_path=''):
    if type(data) != dict:
        return str(data)
    result = []
    for current_property, property_description in data.items():
        pathname = update_pathname(current_path, current_property)
        current_type = property_description.get('type')

        # if the property is new
        if current_type == NEW:
            current_value = get_str_value(property_description)
            entry = "Property '{}' was added with value: '{}'".format(
                pathname, current_value)

        # if the property is nested
        elif current_type == CHILDREN:
            current_value = property_description.get('value')
            entry = render(current_value, pathname)

        # if the property was lost
        elif current_type == LOST:
            entry = "Property '{}' was removed".format(pathname)

        # if the value of property was changed
        elif current_type == CHANGED:
            old_value = property_description.get('old_value')
            new_value = property_description.get('new_value')
            entry = "Property '{}' was changed. From '{}' to '{}'".format(
                pathname, old_value, new_value)
        
        # if the value stays the same
        else:
            continue

        result.append(entry)
    return '\n'.join(result).strip()


def get_str_value(property_description):
    value = property_description.get('value')
    if type(value) == dict:
        return COMPLEX
    else:
        return str(value)


def update_pathname(path, current_property):
    if not path:
        path = current_property
    else:
        path = '{}.{}'.format(path, current_property)
    return path
