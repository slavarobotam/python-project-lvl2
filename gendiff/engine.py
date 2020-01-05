import argparse
from gendiff.parsers import get_parsed_data
from gendiff.build_ast import build_ast
from gendiff.formatters import FORMATTERS, DEFAULT_FORMATTER


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format',
                    default=DEFAULT_FORMATTER,
                    type=str,
                    choices=FORMATTERS.keys(),
                    help='set format of output: "plain", "json", "pretty"')


def generate_diff(first_path, second_path, format=DEFAULT_FORMATTER):
    first_data = get_parsed_data(first_path)
    second_data = get_parsed_data(second_path)
    ast = build_ast(first_data, second_data)
    formatter = FORMATTERS[format]
    rendered_result = formatter.render(ast)
    return rendered_result


def engine(args):
    first_path = args.first_file
    second_path = args.second_file
    format = args.format
    diff = generate_diff(first_path, second_path, format)
    print(diff)
