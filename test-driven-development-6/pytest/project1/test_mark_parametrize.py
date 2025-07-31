'''pytest enables test parametrization at several levels:

pytest.fixture() allows one to parametrize fixture functions.

@pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class. --> bu dosya bunu işliyor.

pytest_generate_tests allows one to define custom parametrization schemes or extensions.'''

import pytest

@pytest.mark.parametrize("a, b, result", [(1,2,3), (4,3,10), (10,10,20)])
def test_add(a,b,result):
    assert a + b == result