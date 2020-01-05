from gendiff.constants import NEW, LOST, SAME, NESTED, CHANGED, SIMPLE


def build_ast(first, second):
    first_keys = first.keys()
    second_keys = second.keys()
    ast = {}

    # create groups of keys
    same_keys = sorted(first_keys & second_keys)
    new_keys = sorted(second_keys - first_keys)
    lost_keys = sorted(first_keys - second_keys)

    # iterate through same_keys to add SAME, CHILDREN and CHANGED to ast
    for key in same_keys:
        first_value = first[key]
        second_value = second[key]
        old_value = None  # parameter used for CHANGED type only
        # if values are equal
        if first_value == second_value:
            type_ = SAME
            value = create_leaf(first_value)
        # if both values are nested
        elif isinstance(first_value, dict) and isinstance(second_value, dict):
            type_ = NESTED
            value = build_ast(first_value, second_value)
        # if the value was changed
        else:
            type_ = CHANGED
            value = create_leaf(second_value)
            old_value = create_leaf(first_value)
        ast[key] = create_node(type_, value, old_value)

    # iterate through new_keys and lost_keys to add NEW and LOST to ast
    for type_, key_set, source in (
        (NEW, new_keys, second),
        (LOST, lost_keys, first),
    ):
        for key in key_set:
            ast[key] = create_node(type_, create_leaf(source[key]))
    return ast


# building node with type SIMPLE if the value is dict
def create_leaf(value):
    if isinstance(value, dict):
        result = create_node(SIMPLE, value)
    else:
        result = value
    return result


def create_node(type_, value, old_value=None):
    if not old_value:
        node = {'type': type_, 'value': value}
    else:
        node = {'type': type_, 'old_value': old_value, 'new_value': value}
    return node
