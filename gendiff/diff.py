#!/usr/bin/env python3

import argparse
from .parsers import get_parsed_data


INDENT = '  '
NEW, LOST, SAME = '+', '-', ' '
CHILDREN = 'children'
CHANGED = 'changed'


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()  # noqa F841
    first = get_parsed_data(args.first_file)
    second = get_parsed_data(args.second_file)
    ast = generate_diff(first, second)
    rendered_result = render(ast)
    return rendered_result


def generate_diff(first, second):  # input two parsed data, output AST
    same_items = {
        key: {
            'type': SAME,
            'value': first[key]}
        for key in first if key in second}
    new_items = {
        key: {
            'type': NEW,
            'value': second[key]}
        for key in second if key not in first}
    lost_items = {
        key: {
            'type': LOST,
            'value': first[key]}
        for key in first if key not in second}
    ast = {}
    for key in same_items:
        if first[key] == second[key]:  # if item remains the same
            ast[key] = {
                'type': SAME,
                'value': first[key]}
        elif isinstance(first[key], dict) and isinstance(second[key], dict):
            ast[key] = {
                'type': CHILDREN,
                'value': generate_diff(first[key], second[key])}
        else:  # if item was changed
            ast[key] = {
                'type': CHANGED,
                'old_value': first[key],
                'new_value': second[key]}
    for key in new_items:  # items that were added
        ast[key] = {
            'type': NEW,
            'value': second[key]}
    for key in lost_items:  # items that were removed
        ast[key] = {
            'type': LOST,
            'value': first[key]}
    return ast


def render(data, level=1):
    if type(data) != dict:
        return str(data)
    result = []
    indent = INDENT * level
    if level == 1:
        result.append('{')
    for key, value in data.items():
        if value.get('type') == CHILDREN:
            result.append('{}{} {}: {{'.format(indent, SAME, key))
            result.append(render(value['value'], level + 2))
            result.append('{}}}'.format(indent + INDENT))
        elif value.get('type') == CHANGED:
            result.append('{}{} {}: {}'.format(
                indent, NEW, key, value['new_value']))
            result.append('{}{} {}: {}'.format(
                indent, LOST, key, value['old_value']))
        else:
            result.append('{}{} {}: {}'.format(
                INDENT * level, value['type'], key, get_value(value, level)))
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
