from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
server = 'http://localhost:4723/wd/hub'
desired_caps = {
    'platformName':'Android',
    'deviceName':'MI_8_UD',
    'appPackage':'com.tencent.mm',
    'appActivity':'com.tencent.mm.ui.LauncherUI'
}
driver = webdriver.Remote(server,desired_caps)
wait = WebDriverWait(driver,20)
login = wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/e80')))
print(login)
print(login.text)
login.click()

phone = wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/l3')))
#phone.send_keys('13199999999')
phone.set_text('13199999999')


