# -*- coding: utf-8 -*-
# @Author : bhl
# @File : conftest.py
import pytest

@pytest.fixture(scope="session")
def connectDB():
    print('sub_demo 连接数据库操作')
    yield
    print('sub_demo 断开数据库操作')

