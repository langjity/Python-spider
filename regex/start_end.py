import re
# 匹配成功
m = re.search('^The', 'The end.')
print(m)
if m is not None:
    print(m.group())			# 运行结果：The
# The在匹配字符串的最后，不匹配
m = re.search('^The', 'end. The')
print(m)
if m is not None:
    print(m.group())
# 匹配成功
m = re.search('The$', 'end. The')
print(m)
if m is not None:
    print(m.group())				# 运行结果：The
m = re.search('The$', 'The end.')
print(m)
if m is not None:
    print(m.group())
# this的左侧必须有边界，成功匹配，this左侧是空格
m = re.search(r'\bthis', "What's this?")
print(m)
if m is not None:
    print(m.group())				# 运行结果：this
# 不匹配，因为this左侧是“s”，没有边界
# 字符串前面的r表示该字符串中的特殊字符（如“\b”）不进行转义
m = re.search(r'\bthis', "What'sthis?")
print(m)
if m is not None:
    print(m.group())
# this的左右要求都有边界，成功匹配，因为this左侧是空格，右侧是问号（?）
m = re.search(r'\bthis\b', "What's this?")
print(m)
if m is not None:
    print(m.group())				# 运行结果：this
# 不匹配，因为this右侧是a，a也是单词，不是边界
m = re.search(r'\bthis\b', "What's thisa")
print(m)
if m is not None:
    print(m.group())
