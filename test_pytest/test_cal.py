import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.parametrize('a,b,expect', [(1, 2, 3), (4, 5, 9)])
    def test_add(self, a, b, expect):
        result = self.cal.add(a, b)
        assert result == expect
