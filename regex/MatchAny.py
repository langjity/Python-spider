import re

s = '.ind'  				# 使用了点（.）符号的文本模式字符串
m = re.match(s, 'bind')		# 匹配成功
if m is not None:
    print(m.group())		# 运行结果：bind
m = re.match(s,'binding')
# 运行结果：<<_sre.SRE_Match object; span=(0, 4), match='bind'>
print("<" + str(m))
m = re.match(s,'bin')		# 匹配失败
print(m)					# 运行结果：None

m = re.search(s,'<bind>')	# 搜索成功
print(m.group())			# 运行结果：bind
# 运行结果：<_sre.SRE_Match object; span=(1, 5), match='bind'>
print(m)

s1 = '3.14'				# 使用了点（.）符号的文本模式字符串
s2 = '3\.14'				# 使用了转义符将点(.)变成真正的点字符
m = re.match(s1, '3.14')	# 匹配成功，因为点字符同样也是一个字符
# 运行结果：<_sre.SRE_Match object; span=(0, 4), match='3.14'>
print(m)
m = re.match(s1, '3314')	# 匹配成功，3和14之间可以是任意字符
# 运行结果：<_sre.SRE_Match object; span=(0, 4), match='3314'>
print(m)

m = re.match(s2, '3.14')	# 匹配成功
# 运行结果：<_sre.SRE_Match object; span=(0, 4), match='3.14'>
print(m)
m = re.match(s2, '3314')	# 匹配失败，因为中间的3并不是点（.）字符
print(m)					# 运行结果：None
