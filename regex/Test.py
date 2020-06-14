import re
s = '\w?wow(\d?)+'			   # 使用了“？”、“+”和“\w”、“\d”的模式字符串
m = re.search(s, 'awow')       # 匹配成功
print(m)
m = re.search(s, 'awow12')	   # 匹配成功
print(m)
m = re.search(s, 'wow12')      # 匹配成功
print(m)
m = re.search(s, 'ow12')       # 匹配失败，因为中间不是“wow”
print(m)
