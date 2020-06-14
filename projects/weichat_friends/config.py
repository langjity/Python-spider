import os

# 平台
PLATFORM = 'Android'

# 设备名称 通过 adb devices -l 获取
DEVICE_NAME = 'MI_8_UD'


# APP包名
APP_PACKAGE = 'com.tencent.mm'

# 入口类名
APP_ACTIVITY = 'com.tencent.mm.ui.LauncherUI'

# Appium服务器地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
# 等待元素加载时间
TIMEOUT = 500

# 微信手机号密码
USERNAME = '请填写用户名'
PASSWORD = '请填写密码'

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

# 滑动间隔
SCROLL_SLEEP_TIME = 1