from tests.confest import setUp

def test_user(setUp):
    person1, person2 = setUp
    assert person1.name == "ali"
    assert person1.role == "admin"
    assert person2.role == "user"
    assert person2.name == "fatma"