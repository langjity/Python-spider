import re								# 导入re模块
m = re.match('hello', 'hello')			# 进行文本模式匹配，匹配成功
if m is not None:
    print(m.group())					# 运行结果：hello
print(m.__class__.__name__)				# 输出m的类名，运行结果：SRE_Match

m = re.match('hello', 'world')			# 进行文本模式匹配，匹配失败，m为None
if m is not None:
    print(m.group())
print(m)								# 运行结果：None
m = re.match('hello', 'hello world') 	# 只要模式从字符串起始位置开始，也可以匹配成功
if m is not None:
    print(m.group())					# 运行结果：hello
# 运行结果：<_sre.SRE_Match object; span=(0, 5), match='hello'>
print(m)
