import pytest
import os

@pytest.fixture()
def test_case_name():
    return os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]

###############################################################################
def test_case1(test_case_name):
    print("Running Test " + test_case_name)
    x = 1
    y = 2
    assert x+y == 3, (test_case_name + "::FAIL") 
    print("Completed Test " + test_case_name)
    return

###############################################################################
def test_case2(test_case_name):
    print("Running Test " + test_case_name)
    x = 5
    y = 5
    assert x==y, (test_case_name + "::FAIL")
    print("Completed Test " + test_case_name)
    return

###############################################################################
def test_case3(test_case_name):
    print("Running Test " + test_case_name)
    x = 3
    y = 4
    assert x==y , (test_case_name + "::FAIL")
    print("Completed Test " + test_case_name)
    return