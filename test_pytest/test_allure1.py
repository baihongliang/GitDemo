import pytest
import allure


# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140', 'Pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    pass


TEST_CASE_link = 'https://github.com/qameta/allure-integrations/issue/8#issuecomment-268313637'


@allure.testcase(TEST_CASE_link, 'Test case title')
def test_with_testcase_link():
    pass


@allure.feature("feature - 类")
class TestAllure:
    @allure.story("成功方法")
    def test_success(self):
        """this test succeeds"""
        with allure.step("step - 成功"):
            print("成功方法")
        assert True

    @allure.step("切换页面")
    def test_switch_pages(self):
        pass

    @allure.story("失败方法")
    def test_failure(self):
        """this test fails"""
        assert False

    @allure.story("跳过方法")
    def test_skip(self):
        """this test is skipped"""
        pytest.skip('for a reason!')

    @allure.story("异常方法")
    def test_broken(self):
        raise Exception('oops')

