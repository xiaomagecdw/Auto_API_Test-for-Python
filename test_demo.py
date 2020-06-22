import allure
import pytest

@allure.feature('测试用例1')
def test_case_01():
    assert 0 != 1

@allure.feature('测试用例2')
def test_case_02():
    assert 0 == 0


if __name__=='__main__':
    pytest.main(['-s','-q','--alluredir','./Report/xml'])