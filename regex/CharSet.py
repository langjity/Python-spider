import re
# 使用字符集，匹配成功
m = re.match('[ab][cd][ef][gh]', 'adfh')
# 运行结果：adfh
print(m.group())
# 使用字符集，匹配成功
m = re.match('[ab][cd][ef][gh]', 'bceg')
# 运行结果：bceg
print(m.group())
# 使用字符集，匹配不成功，因为a和b是或的关系
m = re.match('[ab][cd][ef][gh]', 'abceh')
# 运行结果：None
print(m)
# 字符集和普通文本模式字符串混合使用，匹配成功，ab相当于前缀
m = re.match('ab[cd][ef][gh]', 'abceh')  # 匹配
# 运行结果：abceh
print(m.group())
# 运行结果：<_sre.SRE_Match object; span=(0, 5), match='abceh'>
print(m)
# 使用择一匹配符，匹配成功，abcd和efgh是或的关系，只要满足一个即可
m = re.match('abcd|efgh', 'efgh')  # 匹配
#  运行结果：efgh
print(m.group())
#  运行结果：<_sre.SRE_Match object; span=(0, 4), match='efgh'>
print(m)
