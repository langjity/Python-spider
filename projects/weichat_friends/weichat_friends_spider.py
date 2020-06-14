from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import *


class FriendsSpider():
    # 初始化
    def __init__(self):


        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)


    # 登录微信
    def login_weixin(self):
        # 登录按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/e80')))
        login.click()
        # 手机输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/l3')))
        phone.set_text(USERNAME)
        # 下一步
        next = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/ay8')))
        next.click()
        # 密码
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/l3')))
        password.set_text(PASSWORD)
        # 提交
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/ay8')))
        submit.click()
    # 进入朋友圈
    def enter_friend(self):

        # 选项卡
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/d99')))
        tab.click()

        # 朋友圈
        friends = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/akt')))
        friends.click()
    # 获取朋友圈信息
    def get_friends_info(self):

        while True:
            # 当前页面显示的所有状态
            items = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.ID, 'com.tencent.mm:id/emw')))
            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            # 遍历每条状态
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.tencent.mm:id/b6e').get_attribute('text')
                    # 正文
                    content = item.find_element_by_id('com.tencent.mm:id/d13').get_attribute('text')
                    print(nickname, content)
                    sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass
    # 开启爬虫
    def start(self):

        # 登录
        self.login_weixin()
        # 进入朋友圈
        self.enter_friend()
        # 抓取朋友圈信息
        self.get_friends_info()


if __name__ == '__main__':
    spider = FriendsSpider()
    spider.start()