import pytest
from _pytest.fixtures import fixture

###############################################################################
@pytest.fixture(autouse=True)
def setup():
    return

###############################################################################
@pytest.fixture
def fix_x():
    return 10

###############################################################################
@pytest.fixture
def fix_y():
    return 5

###############################################################################
def test_case1(fix_x,fix_y):
    assert fix_x+fix_y == 15
    return
    
###############################################################################
def test_case2(fix_x,fix_y):
    assert fix_x+fix_y == 15
    return
    


