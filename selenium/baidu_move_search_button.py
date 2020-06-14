from selenium import webdriver
import time
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.get("http://www.baidu.com")
search_button = driver.find_element_by_id("su")  # 百度搜索按钮
# arguments[0]对应的是第一个参数，可以理解为python里的%s传参，与之类似
x_positions = [50,90,130,170]
y_positions = [100,120,160,90]
for i in range(len(x_positions)):
    js = '''
     arguments[0].style.position = "absolute";
     arguments[0].style.left="{}px";
     arguments[0].style.top="{}px";
    '''.format(x_positions[i],y_positions[i])
    driver.execute_script(js, search_button)
    time.sleep(2)
