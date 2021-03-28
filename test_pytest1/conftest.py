# -*- coding: utf-8 -*-
# @Author : bhl
# @File : conftest.py
import os

import pytest
import yaml

from pythoncode.calculator import Calculator


@pytest.fixture(scope="session")
def connectDB():
    print('连接数据库操作')
    yield
    print('断开数据库操作')


# session级别，多个文件只执行一次fixture方法
# 命令行执行：pytest test_feature_scope*.py -sv


@pytest.fixture(scope="class")
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc

# 设置文件的绝对路径，避免子目录访问报错
yaml_file_path = os.path.dirname(__file__) + "/data.yml"
with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas['datas']
    add_ids = datas['myids']
    # return [add_datas, add_ids]

@pytest.fixture(params=add_datas, ids=add_ids)
def get_datas(request):
    print('开始计算')
    data = request.param
    print(f'request.param的测试数据是{data}')
    yield data
    print('结束计算')