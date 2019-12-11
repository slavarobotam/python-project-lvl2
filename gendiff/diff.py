#!/usr/bin/env python3

import argparse
from .parsers import get_parsed_data


INDENT = '  '
NEW, LOST, SAME = '+', '-', ' '
NESTED = 'N'
CHANGED = 'CH'


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
    same_key_items = {key: {'type': SAME, 'value': first[key]} for key in first if key in second}
    new_key_items = {key: {'type': NEW, 'value': second[key]} for key in second if key not in first}
    lost_key_items = {key: {'type': LOST, 'value': first[key]} for key in first if key not in second}
    ast = {}
    for key in same_key_items:
        if first[key] == second[key]:
            ast[key] = {'type': SAME, 'value': first[key]}
        elif isinstance(first[key], dict) and isinstance(second[key], dict):
            ast[key] = {'type': NESTED, 'value': generate_diff(first[key], second[key])}            
        else:
            ast[key] = {'type': CHANGED, 'old_value': first[key], 'new_value': second[key]}
    for key in new_key_items:
        ast[key] = {'type': NEW, 'value': second[key]}
    for key in lost_key_items:
        ast[key] = {'type': LOST, 'value': first[key]}
    return ast

def render(item, level=1):
        result = []
        if level == 1:
            result.append('{')
            indent = INDENT
        else:
            indent = INDENT * level + INDENT
        for key, value in item.items():
            if isinstance(value, dict):
                if value.get('type') == NESTED:
                    result.append('{}{} {}: {{'.format(indent, SAME, key))
                    result.append(render(value['value'], level+1))
                    result.append('{}}}'.format(indent+ INDENT))
                elif value.get('type') == CHANGED:
                    result.append('{}{} {}: {}'.format(indent, NEW, key, value['new_value']))
                    result.append('{}{} {}: {}'.format(indent, LOST, key, value['old_value']))
                else:
                    result.append('{}{} {}: {}'.format(indent, value['type'], key, get_value(value, level)))
        if level == 1:
            result.append('}')
        return '\n'.join(result)


def get_value(value, level=1):
    res = ''
    if isinstance(value, dict) and 'type' not in value:
        res += ('{\n')
        for k, v in value.items():
            res += ('{}{}: {}\n'.format(INDENT*level + INDENT*level, k, v))
        if level >=2:
            res += ('{}}}'.format(INDENT*level+INDENT*(level-2)))
        else:
            res += ('{}}}'.format(INDENT*level))
    elif isinstance(value, dict) and 'type' in value:
        res = get_value(value['value'], level+1)
    else:
        res = str(value)
    return res
