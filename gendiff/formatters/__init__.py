from gendiff.formatters import plain, json, pretty


FORMATTERS = {
    'plain': plain,  # noqa: F821
    'json': json,  # noqa: F821
    'pretty': pretty  # noqa: F821
}

DEFAULT_FORMATTER = 'pretty'
