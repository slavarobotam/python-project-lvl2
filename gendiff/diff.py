#!/usr/bin/env python3

import argparse
from .parsers import get_parsed_data
from gendiff.formatters import undefined, plain

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
    format = args.format
    ast = generate_diff(first, second)
    if format == 'plain':
        formatter = plain
    else:
        formatter = undefined
    rendered_result = formatter.render(ast)
    return rendered_result


def generate_diff(first, second):
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
