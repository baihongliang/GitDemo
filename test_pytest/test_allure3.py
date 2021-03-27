import allure
import pytest
from selenium import webdriver
import time

@allure.testcase("https:github.com","管理测试用例URL")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data", ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data):
    with allure.step("打开百度"):
        driver = webdriver.Chrome("/Users/baihongliang/software/chromedriver")
        driver.get("https://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入关键字：{test_data}"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./image/b.png")
        allure.attach.file("./image/b.png",'保存图片', attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()
