#!/usr/bin/env python3

import argparse
from .parsers import parse_file


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()  # noqa F841
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


def generate_diff(path1, path2, format):
    file1 = parse_file(path1)
    file2 = parse_file(path2)
    same_key_items = {key: file1[key] for key in file1 if key in file2}
    new_key_items = {key: file2[key] for key in file2 if key not in file1}
    lost_key_items = {key: file1[key] for key in file1 if key not in file2}
    NEW, LOST, SAME = '+', '-', ' '
    changelist = []
    for key in same_key_items:
        if file1[key] == file2[key]:
            changelist.append('{} {}: {}'.format(SAME, key, file1[key]))
        else:
            changelist.append('{} {}: {}'.format(NEW, key, file2[key]))
            changelist.append('{} {}: {}'.format(LOST, key, file1[key]))
    for key in new_key_items:
        changelist.append('{} {}: {}'.format(NEW, key, file2[key]))
    for key in lost_key_items:
        changelist.append('{} {}: {}'.format(LOST, key, file1[key]))
    result_string = '\n  '.join(changelist)
    begin = '{\n  '
    end = '\n}'
    return '{}{}{}'.format(begin, result_string, end)
