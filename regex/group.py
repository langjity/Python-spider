import re
# 分成3组：(\d{3})、(\d{4})和([a-z]{2})
m = re.match('(\d{3})-(\d{4})-([a-z]{2})', '123-4567-xy')

if m is not None:
    print(m.group())		# 运行结果：123-4567-xy
    print(m.group(1))		# 获取第1组的值，运行结果：123
    print(m.group(2))		# 获取第2组的值，运行结果：4567
    print(m.group(3))         # 获取第3组的值，运行结果：xy
    print(m.groups())         # 获取每组的值组成的元组，运行结果：('123', '4567', 'xy')
print('-----------------')
# 分成2组：(\d{3}-\d{4})和([a-z]{2})
m = re.match('(\d{3}-\d{4})-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())		# 运行结果：123-4567-xy
    print(m.group(1))		# 获取第1组的值，运行结果：123-4567
    print(m.group(2))		# 获取第2组的值，运行结果：xy
    print(m.groups())         # 获取每组的值组成的元组，运行结果：('123-4567', 'xy')
print('-----------------')
# 分了1组：([a-z]{2})
m = re.match('\d{3}-\d{4}-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())		# 运行结果：123-4567-xy
    print(m.group(1))		# 获取第1组的值，运行结果：xy
print(m.groups())		# 获取每组的值组成的元组，运行结果：('xy',)
print('-----------------')
# 未分组，因为模式字符串中没有圆括号括起来的部分
m = re.match('\d{3}-\d{4}-[a-z]{2}', '123-4567-xy')
if m is not None:
    print(m.group())		# 运行结果：123-4567-xy
    print(m.groups())		# 获取每组的值组成的元组，运行结果：()
