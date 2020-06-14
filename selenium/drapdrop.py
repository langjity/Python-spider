from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome('./webdriver/chromedriver')
try:
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
except Exception as e:
    print(e)
    browser.close()