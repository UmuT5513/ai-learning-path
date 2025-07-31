import pytest
from main import func

@pytest.mark.sadecetrueolanlar
def test_func():
    assert func(1) == 2

def test_func2():
    assert func(2) == 4

@pytest.mark.sadecetrueolanlar
def test_func3():
    assert func(3) == 4

def test_func4():
    assert func(4) == 8

@pytest.mark.sadecetrueolanlar
def test_func5():
    assert func(5) == 6

