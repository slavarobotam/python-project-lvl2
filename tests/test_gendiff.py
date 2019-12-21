# -*- coding:utf-8 -*-

"""Test correctness of function generating difference."""

import pytest  # noqa: F401
from gendiff import generate_diff, get_parsed_data
import tests.fixtures.expected_results as expected
from gendiff.formatters import undefined, plain, json


@pytest.fixture()
def paths():
    first = './tests/fixtures/before.json'
    second = './tests/fixtures/after.json'
    return first, second


def test_plain_json():
    first = './tests/fixtures/before.json'
    second = './tests/fixtures/after.json'
    first = get_parsed_data(first)
    print('first', first)
    print('expected.PLAIN_JSON:\n', expected.PLAIN_JSON)
    second = get_parsed_data(second)
    ast = generate_diff(first, second)
    result = undefined.render(ast)
    print('result:\n', result)
    assert result == expected.PLAIN_JSON


def test_plain_yaml():
    first = './tests/fixtures/before.yml'
    second = './tests/fixtures/after.yml'
    first = get_parsed_data(first)
    second = get_parsed_data(second)
    print('first', first)
    print('second', second)
    print('expected.PLAIN_YAML:\n', expected.PLAIN_YAML)
    ast = generate_diff(first, second)
    result = undefined.render(ast)
    print('result:\n', result)
    assert result == expected.PLAIN_YAML


def test_complex_json():
    first = './tests/fixtures/complex_before.json'
    second = './tests/fixtures/complex_after.json'
    first = get_parsed_data(first)
    second = get_parsed_data(second)
    print('expected.PLAIN_YAML:\n', expected.COMPLEX_JSON)
    ast = generate_diff(first, second)
    result = undefined.render(ast)
    print('result:\n', result)
    assert expected.COMPLEX_JSON == result


def test_plain_format():
    first = './tests/fixtures/complex_before.json'
    second = './tests/fixtures/complex_after.json'
    first = get_parsed_data(first)
    second = get_parsed_data(second)
    print('expected.PLAIN_FORMAT:\n', expected.PLAIN_FORMAT)
    ast = generate_diff(first, second)
    result = plain.render(ast)
    print('result:\n', result)
    assert expected.PLAIN_FORMAT == result


def test_json_format():
    first = './tests/fixtures/complex_before.json'
    second = './tests/fixtures/complex_after.json'
    first = get_parsed_data(first)
    second = get_parsed_data(second)
    print('expected.JSON_FORMAT:\n', expected.JSON_FORMAT)
    ast = generate_diff(first, second)
    result = json.render(ast)
    print('result:\n', result)
    assert expected.JSON_FORMAT == result
