import re
s = 'Bill|Mike|John'				# 指定使用择一匹配符号的文本模式字符串
m = re.match(s, 'Bill')				# 匹配成功
if m is not None:
    print(m.group())				# 运行结果：Bill
m = re.match(s, "Bill:my friend")	# 匹配成功
if m is not None:
    print(m.group())				# 运行结果：Bill

m = re.search(s,'Where is Mike?')	# 搜索成功
if m is not None:
    print(m.group())				# 运行结果：Mike
# 运行结果：<_sre.SRE_Match object; span=(9, 13), match='Mike'>
print(m)
