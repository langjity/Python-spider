from selenium import webdriver
from selenium.webdriver import ActionChains
import time
browser = webdriver.Chrome('./webdriver/chromedriver')
try:
    browser.get('https://www.jd.com')
    actions = ActionChains(browser)

    li_list = browser.find_elements_by_css_selector(".cate_menu_item")

    for li in li_list:
        actions.move_to_element(li).perform()
        time.sleep(1)
except Exception as e:
    print(e)
    browser.close()