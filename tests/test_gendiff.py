# -*- coding:utf-8 -*-

"""Test correctness of function generating difference."""

import pytest  # noqa: F401
from gendiff import generate_diff, get_parsed_data
import tests.fixtures.expected_results as expected
from gendiff.formatters import pretty, plain, json


@pytest.fixture()
def json_paths():
    return {
        'before': './tests/fixtures/before.json',
        'after': './tests/fixtures/after.json',
        'complex_before': './tests/fixtures/complex_before.json',
        'complex_after': './tests/fixtures/complex_after.json'
        }


@pytest.fixture()
def yaml_paths():
    return {
        'before': './tests/fixtures/before.yml',
        'after': './tests/fixtures/after.yml',
        }


def get_ast(first_path, second_path):  # gets two str paths and returns AST
    first = get_parsed_data(first_path)
    second = get_parsed_data(second_path)
    ast = generate_diff(first, second)
    return ast


def test_plain_json(json_paths):
    first = json_paths['before']
    second = json_paths['after']
    ast = get_ast(first, second)
    result = pretty.render(ast)
    assert expected.PLAIN_JSON == result


def test_plain_yaml(yaml_paths):
    first = yaml_paths['before']
    second = yaml_paths['after']
    ast = get_ast(first, second)
    result = pretty.render(ast)
    assert expected.PLAIN_YAML == result


def test_complex_json(json_paths):
    first = json_paths['complex_before']
    second = json_paths['complex_after']
    ast = get_ast(first, second)
    result = pretty.render(ast)
    assert expected.COMPLEX_JSON == result


def test_plain_format(json_paths):
    first = json_paths['complex_before']
    second = json_paths['complex_after']
    ast = get_ast(first, second)
    result = plain.render(ast)
    assert expected.PLAIN_FORMAT == result


def test_json_format(json_paths):
    first = json_paths['complex_before']
    second = json_paths['complex_after']
    ast = get_ast(first, second)
    result = json.render(ast)
    assert expected.JSON_FORMAT == result
