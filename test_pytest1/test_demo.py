# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_demo.py
import pytest
import yaml


class TestCalc:

    # @pytest.mark.parametrize('a,b,expect',[(1,1,2),(2,2,4)])
    def test_add(self, get_calc, get_datas):
        assert get_datas[2] == get_calc.add(get_datas[0], get_datas[1])
