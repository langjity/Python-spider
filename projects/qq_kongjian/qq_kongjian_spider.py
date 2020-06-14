from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome('chromedriver',options=options)
browser.maximize_window()

def get_info(qq):
    browser.get('http://user.qzone.qq.com/{}/311'.format(qq))

    browser.switch_to.frame('login_frame')
    browser.find_element_by_id('switcher_plogin').click()
    browser.find_element_by_id('u').clear()
    browser.find_element_by_id('u').send_keys(qq)
    browser.find_element_by_id('p').clear()
    browser.find_element_by_id('p').send_keys('QQ密码')
    browser.find_element_by_id('login_button').click()
    
    time.sleep(3)

    browser.switch_to.frame('app_canvas_frame')
    contents = browser.find_elements_by_css_selector('.content')
    times = browser.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
    for content, tim in zip(contents, times):
        data = {
            'time': tim.text,
            'content': content.text
        }
        print(data)


if __name__ == '__main__':
    get_info('QQ号')
