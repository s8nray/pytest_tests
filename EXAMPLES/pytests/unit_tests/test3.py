class TestClass:
    def test_one_a(self):
        x = "hat"
        assert "h" in x

    def test_two_b(self):
        x = "cap"
        assert hasattr(x, "check")

    def test_three_c(self):
        x = "nice"
        assert "i" in x

    def test_four_d(self):
        x = "true"
        assert "u" in x

    def test_five_e(self):
        x = "people"
        assert "o" in x