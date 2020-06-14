
from selenium import webdriver
browser = webdriver.Chrome('./webdriver/chromedriver')
browser.get('https://www.jd.com')
print(browser.get_cookies())
browser .add_cookie({'name': 'name',
 'value':'jd','domain':'www.jd.com'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())  # 大部分删除了，可能还剩下一些


