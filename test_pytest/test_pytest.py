import pytest


def test_aa():
    print(111)
    pass


def add(a, b) -> int:
    return a + b


@pytest.mark.demo
@pytest.mark.parametrize('a', [1, 2, 3], ids=['a', 'b', 'c'])
@pytest.mark.parametrize('b', [1, 2, 3], ids=['d','e','f'])
def test_add(a, b):
    print(f"测试参数堆叠组合:a->{a},b->{b}")


@pytest.mark.smoke
@pytest.mark.parametrize('a,b,expected', [
    (2, 3, 5),
    (1, 4, 5),
    (1, 5, 6)
], ids=['int', 'int2', 'int3'])
def test_add2(a, b, expected):
    assert expected == add(a, b)


class TestDemo:
    def test_a(self):
        print("a")


@pytest.fixture()
def login():
    username = "xiaoming"
    return username


@pytest.mark.skip
class TestLogin:
    def test_login(self, login):
        print(f'a username= {login}')

    def test_eat(self):
        print('eat')

    def test_login_eat(self, login):
        print(f'{login} eat')


if __name__ == '__main__':
    # pytest.main()
    # pytest.main(['test_pytest.py'])
    pytest.main(['test_pytest.py', '-sv'])
    # pytest.main(['test_pytest.py::TestDemo'])
