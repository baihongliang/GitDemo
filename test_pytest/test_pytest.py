import pytest


def test_aa():
    print(111)
    pass


def add(a, b) -> int:
    return a + b


def test_add():
    assert 5 == add(2, 3)


@pytest.mark.parametrize('a,b',[
    (2,3),
    (1,4),
    (1,5)
])
def test_add2(a,b):
    assert 5 == add(a, b)

class TestDemo:
    def test_a(self):
        print("a")

@pytest.fixture()
def login():
    username = "xiaoming"
    return username

class TestLogin:
    def test_login(self, login):
        print(f'a username= {login}')

    def test_eat(self):
        print('eat')

    def test_login_eat(self,login):
        print(f'{login} eat')


if __name__ == '__main__':
    # pytest.main()
    # pytest.main(['test_pytest.py'])
    pytest.main(['test_pytest.py', '-v'])
    # pytest.main(['test_pytest.py::TestDemo'])
