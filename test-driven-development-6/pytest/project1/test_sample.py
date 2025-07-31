from main import func
import pytest

@pytest.mark.xfail
def test_func():
    assert func(1) == 3


