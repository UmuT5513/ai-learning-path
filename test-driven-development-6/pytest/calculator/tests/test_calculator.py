from calculator import topla, cikar, carp, bol
import pytest
def test_topla():
    assert topla(2,2) == 4

def test_cikar():
    assert cikar(3,1) == 2

def test_carp():
    assert carp(2,5) == 10

@pytest.mark.bolme
def test_bol():
    assert bol(10,2) == 5

@pytest.mark.bolme
def test_bol_zero_division():
    '''paydanın 0 olması durumunda hata fırlatıp fırlatmıyor munun testi.'''
    with pytest.raises(ZeroDivisionError):
        bol(5,0)

@pytest.mark.bolme
def test_bol_negative():
    assert bol(4,-2) == -2

@pytest.mark.bolme
def test_bol_invalid_input():
    """Test that bol raises a TypeError when the input is not a valid number."""
    with pytest.raises(TypeError):
        bol("5", 1)