# Grouping tests in classes can be beneficial for the following reasons:

# Test organization

# Sharing fixtures for tests only in that particular class

# Applying marks at the class level and having them implicitly apply to all tests


from main import one,func

class TestClass: # class ismi Test... diye gitmeli.
    def test_one(self):
        assert "h" in one()

    def test_func(self):
        assert func(1) == 2
