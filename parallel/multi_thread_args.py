import random
from time import sleep
import _thread as thread
# 线程函数，其中a和b是通过start_new_thread函数传入的参数
def fun(a,b):
    print(a,b)
    # 随机休眠一个的时间（1到4秒）
    sleep(random.randint(1,5))
#  启动8个线程
for i in range(8):
    # 为每一个线程函数传入2个参数值
    thread.start_new_thread(fun, (i + 1,'a' * (i + 1)))
# 通过从终端输入一个字符串的方式让程序暂停
input()
