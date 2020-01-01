import argparse
from gendiff.parsers import get_parsed_data
from gendiff.diff import generate_diff
from gendiff.formatters.get_formatter import get_formatter


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format',
                    default='pretty',
                    type=str,
                    choices=['plain', 'json', 'pretty'],
                    help='set format of output: "plain", "json", "pretty"')


def gendiff(args):
    first = get_parsed_data(args.first_file)
    second = get_parsed_data(args.second_file)
    ast = generate_diff(first, second)
    formatter = get_formatter(args.format)
    rendered_result = formatter.render(ast)
    print(rendered_result)
