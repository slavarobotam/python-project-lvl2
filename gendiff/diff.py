from gendiff.constants import NEW, LOST, SAME, CHILDREN, CHANGED


def generate_diff(first, second):
    first_keys = first.keys()
    second_keys = second.keys()
    ast = {}

    # create groups of keys
    same_keys = [key for key in first_keys if key in second_keys]
    new_keys = [key for key in second_keys if key not in first_keys]
    lost_keys = [key for key in first_keys if key not in second_keys]

    # iterate through same_keys to add SAME, CHILDREN and CHANGED to ast
    for key in same_keys:
        first_value = first[key]
        second_value = second[key]
        old_value = None  # parameter used for CHANGED type only
        # if values are equal
        if first_value == second_value:
            type_ = SAME
            value = first_value
        # if both values are nested
        elif isinstance(first_value, dict) and isinstance(second_value, dict):
            type_ = CHILDREN
            value = generate_diff(first_value, second_value)
        # if the value was changed
        else:
            type_ = CHANGED
            value = second_value
            old_value = first_value
        ast[key] = create_node(type_, value, old_value)

    # iterate through new_keys and lost_keys to add NEW and LOST to ast
    for type_, key_set, source in (
        (NEW, new_keys, second),
        (LOST, lost_keys, first),
    ):
        for key in key_set:
            ast[key] = {
                'type': type_,
                'value': source[key]
            }
    return ast


def create_node(type_, value, old_value=None):
    if not old_value:
        node = {'type': type_, 'value': value}
    else:
        node = {'type': type_, 'old_value': old_value, 'new_value': value}
    return node
