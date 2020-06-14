from selenium import webdriver
import time
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.get("https://www.jd.com")
ul = driver.find_element_by_id('navitems-group1')
li_list = ul.find_elements_by_tag_name('li')
a1 = li_list[0].find_element_by_tag_name('a')
a2 = li_list[1].find_element_by_tag_name('a')
js = '''
 arguments[0].text = 'Python从菜鸟到高手'
 arguments[0].href = 'https://item.jd.com/12417265.html'
 arguments[1].text = '极客起源'
 arguments[1].href = 'https://geekori.com'
 '''
driver.execute_script(js, a1,a2)

