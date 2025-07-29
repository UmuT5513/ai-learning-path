from main import Person

def setUp():
    return Person("John", 10)
def test_name():
    p = setUp()
    assert p.get_name() == "John"

def test_age():
    p = setUp()
    assert p.get_age() == 10