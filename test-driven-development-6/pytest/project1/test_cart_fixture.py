import pytest

@pytest.fixture()
def setUp():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")

def test_AddItemtoCart(setUp):
    print("Add Item Successful")

def test_RemoveItemFromCart(setUp):
    print("Remove Item Successful")
