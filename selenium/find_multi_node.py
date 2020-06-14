from selenium import webdriver
from selenium.webdriver.common.by import By
# 不支持本地网页
browser = webdriver.Chrome('./webdriver/chromedriver')
try:
    browser.get('https://www.jd.com')
    input = browser.find_elements_by_tag_name('li')

    print(input)
    print(len(input))
    print(input[0].text)
    input = browser.find_elements(By.TAG_NAME,'ul')
    print(input)
    print(input[0].text)
    
    browser.close()

except Exception as e:
    print(e)
    browser.close()