import pytest
import yaml


def get_data():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas['datas']
        add_ids = datas['myids']
        return [add_datas, add_ids]


class TestDemo:

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./data1.yml")))
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

    # @pytest.mark.parametrize('a,b,expected',[(1,1,2),(2,2,4)])
    # @pytest.mark.parametrize('a,b,expected',yaml.safe_load(open("./data.yml")).get('datas'))
    @pytest.mark.parametrize('a,b,expected', yaml.safe_load(open("./data.yml"))['datas'],
                             ids=yaml.safe_load(open("./data.yml"))['myids'])
    def test_param4(self, a, b, expected):
        assert a + b == expected

    @pytest.mark.parametrize('a,b,expected', get_data()[0], ids=get_data()[1])
    def test_param5(self,a, b, expected):
        assert a + b == expected
