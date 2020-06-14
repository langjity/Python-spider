from selenium import webdriver
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome('./webdriver/chromedriver',chrome_options=options)
#browser = webdriver.PhantomJS('./webdriver/phantomjs')
browser.get('https://www.jd.com')
ul = browser.find_element_by_id("navitems-group1")
print(ul.text)
print('id','=',ul.id)  # 内部id，不是节点id属性值
print('location','=',ul.location)

print('tag_name','=',ul.tag_name)
print('size','=',ul.size)
li_list = ul.find_elements_by_tag_name("li")
for li in li_list:
    print(type(li))
    # 属性没找到，返回None
    print('<',li.text,'>', 'class=',li.get_attribute('class'))
    a = li.find_element_by_tag_name('a')
    print('href','=',a.get_attribute('href'))
browser.close()