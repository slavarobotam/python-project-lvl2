# -*- coding:utf-8 -*-

"""Test correctness of function generating difference."""

import pytest  # noqa: F401
from gendiff.engine import gendiff

DATA_SETS_FOR_TESTCASES = {
            'plain_json': 'plain_json_paths',
            'plain_yaml': 'plain_yaml_paths',
            'complex_json': 'complex_json_paths',
            'format_json': 'complex_json_paths',
            'format_plain': 'complex_json_paths'
}

DATA_SET_FILEPATHS = {
        'plain_json_paths': (
            'tests/fixtures/before.json',
            'tests/fixtures/after.json'),
        'plain_yaml_paths': (
            'tests/fixtures/before.yml',
            'tests/fixtures/after.yml'),
        'complex_json_paths': (
            'tests/fixtures/complex_before.json',
            'tests/fixtures/complex_after.json')
}

EXPECTED_RESULTS_PATHS = {
        'plain_json': 'tests/fixtures/expected_for_plain_json.txt',
        'plain_yaml': 'tests/fixtures/expected_for_plain_yaml.txt',
        'complex_json': 'tests/fixtures/expected_for_complex_json.txt',
        'format_plain': 'tests/fixtures/expected_format_plain.txt',
        'format_json': 'tests/fixtures/expected_format_json.json'
}


@pytest.fixture()
def expected_results():
    def get_expected_result(testcase):
        filepath = EXPECTED_RESULTS_PATHS[testcase]
        with open(filepath) as file:
            return file.read()
    return get_expected_result


@pytest.fixture()
def data_sets():
    def get_filepaths(testcase):
        data_set = DATA_SETS_FOR_TESTCASES[testcase]
        return DATA_SET_FILEPATHS[data_set]
    return get_filepaths


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
