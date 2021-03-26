import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./data.yaml")))
    def test_param(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(('a', 'b'), [
        (10, 20),
        (10, 30)
    ])
    def test_param3(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(['a', 'b'], [
        (10, 20),
        (10, 30)
    ])
    def test_param2(self, a, b):
        print(a + b)

    @pytest.mark.parametrize('a,b', [
        (10, 20),
        (10, 30)
    ])
    def test_param1(self, a, b):
        print(a + b)
