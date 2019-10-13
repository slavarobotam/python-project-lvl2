# -*- coding:utf-8 -*-

"""Test correctness of function generating difference."""

import pytest
from gendiff import generate_diff
import tests.fixtures.expected_results as expected


# @pytest.fixture()
# def paths():
#     file1 = './tests/fixtures/before.json'
#     file2 = './tests/fixtures/after.json'
#     return file1, file2
def test_one():
    file1 = './tests/fixtures/before.json'
    file2 = './tests/fixtures/after.json'
    assert generate_diff(file1, file2) == expected.PLAIN_JSON
