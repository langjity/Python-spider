from selenium import webdriver
from selenium.webdriver.common.by import By
# 不支持本地网页
browser = webdriver.Chrome('./webdriver/chromedriver')
try:
    browser.get('http://localhost/demo.html')
    input = browser.find_element_by_id('name')
    input.send_keys('王军')
    input = browser.find_element_by_id('age')
    input.send_keys('30')

    input = browser.find_element_by_name('country')
    input.send_keys('中国')

    input = browser.find_element_by_class_name('myclass')
    input.send_keys('4000')

    # 或下面的代码
    input = browser.find_element(By.CLASS_NAME,'myclass')
    input.clear()  # 不清空  追加
    input.send_keys('8000')



except Exception as e:
    print(e)
    browser.close()