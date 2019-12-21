#!/usr/bin/env python3

import argparse
from .parsers import get_parsed_data
from .diff import generate_diff
from gendiff.formatters.get_formatter import get_formatter


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()  # noqa F841
    first = get_parsed_data(args.first_file)
    second = get_parsed_data(args.second_file)
    ast = generate_diff(first, second)
    formatter = get_formatter(args.format)
    rendered_result = formatter.render(ast)
    print(rendered_result)
