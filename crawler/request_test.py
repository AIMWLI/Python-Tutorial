import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def request_get_test():
    response = requests.get("https://www.baidu.com")
    print("---code " + str(response.status_code))  # 200
    print(
        "---text " + response.text)  # HTTP响应的内容。通常情况下，它会解码为Unicode字符串，并且是根据HTTP响应的Content-Type头来确定的。如果响应是一个HTML页面，response.text将返回HTML文本；如果是JSON数据，它将返回JSON格式的字符串。
    print("---content " + str(response.content))  # 这是一个字节对象，包含了原始的HTTP响应内容。
    print(response.url)
    print(response.cookies)
    print(response.headers)
    print(response.elapsed)


def request_post_test():
    data = {"word": "hello"}
    response = requests.post("http://httpbin.org/post", data=data)
    print(response.text)


def request_find_ip():
    proxy = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
    url = "https://www.ip.cn/api/index?ip=&type=0"
    response = requests.get(url, proxies=proxy)
    data = response.json()
    print(data.get("ip"))


def request_find_ip_by_chrome():
    # 创建Chrome浏览器选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无窗口模式
    # 创建浏览器对象
    driver = webdriver.Chrome(options=chrome_options)
    # 打开网页
    url = "https://www.ip.cn/"
    driver.get(url)
    time.sleep(4)  # 加载等待
    try:
        # 等待目标元素加载完成，最长等待时间为10秒
        search_box = driver.find_element(By.XPATH, "//*[@id='tab0_ip']")
        # 提取IP地址
        ip_address = search_box.text
        print("你的IP地址是：", ip_address)
    finally:
        driver.quit()


if __name__ == '__main__':
    # request_get_test()
    # request_post_test()
    request_find_ip()
    # request_find_ip_by_chrome()
