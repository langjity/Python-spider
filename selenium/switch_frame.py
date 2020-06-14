import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
'''

有一类节点叫iframe，也就是Frame，结构与外部网页的结构完全一致，如果页面中包含子Frame。是不能获取子Frame中的节点的，所以需要
使用switch_to.frame切换
'''
browser = webdriver.Chrome('./webdriver/chromedriver')
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_elements_by_class_name('logo')
except NoSuchElementException:
    print('没有这个节点')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)