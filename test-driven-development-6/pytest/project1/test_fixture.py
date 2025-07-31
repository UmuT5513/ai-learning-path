'''pytest enables test parametrization at several levels:

pytest.fixture() allows one to parametrize fixture functions.--> bu dosya bunu işliyor.

@pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class.

pytest_generate_tests allows one to define custom parametrization schemes or extensions.'''

import pytest

@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def setUp(request):
    print(request.param)

def test_login(setUp):
    print("Login Successful")