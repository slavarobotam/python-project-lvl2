# -*- coding:utf-8 -*-

"""Test correctness of function generating difference."""

import pytest  # noqa: F401
from gendiff.engine import gendiff


@pytest.fixture()
def expectations_paths():
    return {
        'plain_json': 'tests/fixtures/expected_for_plain_json.txt',
        'plain_yaml': 'tests/fixtures/expected_for_plain_yaml.txt',
        'complex_json': 'tests/fixtures/expected_for_complex_json.txt',
        'format_plain': 'tests/fixtures/expected_format_plain.txt',
        'format_json': 'tests/fixtures/expected_format_json.json'
    }


@pytest.fixture()
def expected_results(expectations_paths):
    def get_expected_result(testcase):
        filepath = expectations_paths[testcase]
        with open(filepath) as file:
            return file.read()
    return get_expected_result


@pytest.fixture()
def input_filepaths():
    return {
        'plain_json': (
            'tests/fixtures/before.json',
            'tests/fixtures/after.json'),
        'plain_yaml': (
            'tests/fixtures/before.yml',
            'tests/fixtures/after.yml'),
        'complex_json': (
            'tests/fixtures/complex_before.json',
            'tests/fixtures/complex_after.json')
    }


@pytest.fixture()
def data_sets(input_filepaths):
    def get_data_set(testcase):
        data_sets = {
            'plain_json': 'plain_json',
            'plain_yaml': 'plain_yaml',
            'complex_json': 'complex_json',
            'format_json': 'complex_json',
            'format_plain': 'complex_json'
        }
        return input_filepaths[data_sets[testcase]]
    return get_data_set


def test_plain_json(data_sets, expected_results):
    testcase = 'plain_json'
    format = 'pretty'
    first, second = data_sets(testcase)
    expected_result = expected_results(testcase)
    result = gendiff(first, second, format)
    assert expected_result == result


def test_plain_yaml(data_sets, expected_results):
    testcase = 'plain_yaml'
    format = 'pretty'
    first, second = data_sets(testcase)
    expected_result = expected_results(testcase)
    result = gendiff(first, second, format)
    assert expected_result == result


def test_complex_json(data_sets, expected_results):
    testcase = 'complex_json'
    format = 'pretty'
    first, second = data_sets(testcase)
    expected_result = expected_results(testcase)
    result = gendiff(first, second, format)
    assert expected_result == result


def test_format_plain(data_sets, expected_results):
    testcase = 'format_plain'
    format = 'plain'
    first, second = data_sets(testcase)
    expected_result = expected_results(testcase)
    result = gendiff(first, second, format)
    assert expected_result == result


def test_format_json(data_sets, expected_results):
    testcase = 'format_json'
    format = 'json'
    first, second = data_sets(testcase)
    expected_result = expected_results(testcase)
    result = gendiff(first, second, format)
    assert expected_result == result
