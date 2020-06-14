from snownlp import SnowNLP

s = SnowNLP('坑！买的纸质+电子书，结果只收到电子书的，纸质就没发货，也联系不到客服。')
s1 = SnowNLP('这本书分成好，赞一个，5分满分，Yeah')
print(s.words)
print("s的情感指数：",s.sentiments )
print("s1的情感指数：",s1.sentiments )
print(s.keywords(3))
print(s.summary(3))

