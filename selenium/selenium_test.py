# coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def setup_driver():
    # 创建Chrome浏览器选项
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # 无窗口模式
    chrome_options.add_argument('--disable-gpu')  # 如果需要

    # 创建浏览器对象
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def search_baidu(driver, query):
    try:
        driver.get('https://www.baidu.com/')  # 打开网页
        time.sleep(1)  # 加载等待

        # 查找搜索框并输入文本
        # search_box = driver.find_element(By.XPATH, "//input[@id='kw']")
        search_box = driver.find_element(By.XPATH, "//*[@id='kw']")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)  # 模拟按下回车键进行搜索

        # 或者使用点击按钮的方式
        # search_button = driver.find_element(By.XPATH, "//*[@id='su']")
        # search_button.click()

        time.sleep(2)  # 等待搜索结果加载
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == '__main__':
    query = "魅族"
    driver = setup_driver()
    search_baidu(driver, query)
