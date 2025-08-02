from user import User
import pytest

@pytest.fixture
def setUp():
    person1 = User("ali", "admin")
    person2 = User("fatma", "user")
    return person1, person2