class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_three(self):
        x = "hello"
        assert "h" in x

    def test_four(self):
        x = "yes"
        assert "y" in x

    def test_five(self):
        x = "nope"
        assert "o" in x