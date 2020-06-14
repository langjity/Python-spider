import re
# 待匹配的字符串
s = '12-a-abc54-a-xyz---78-A-ytr'
# 匹配以2个数字开头，结尾是3个小写字母，中间用“-a”分隔的字符串，对大小写敏感
# 下面的代码都使用了同样的模式字符串
result = re.findall(r'\d\d-a-[a-z]{3}',s)
# 运行结果：['12-a-abc', '54-a-xyz']
print(result)
# 将模式字符串加了两个分组（用圆括号括起来的部分），findall方法也会以分组形式返回
result = re.findall(r'(\d\d)-a-([a-z]{3})',s)
# 运行结果：[('12', 'abc'), ('54', 'xyz')]
print(result)
# 忽略大小写（最后一个参数值：re.I）
result = re.findall(r'\d\d-a-[a-z]{3}',s,re.I)
# 运行结果：['12-a-abc', '54-a-xyz', '78-A-ytr']
print(result)
# 忽略大小写，并且为模式字符串加了2个分组
result = re.findall(r'(\d\d)-a-([a-z]{3})',s,re.I)
# 运行结果：[('12', 'abc'), ('54', 'xyz'), ('78', 'ytr')]
print(result)
# 使用finditer函数匹配模式字符串，并返回匹配迭代器
it = re.finditer(r'(\d\d)-a-([a-z]{3})',s,re.I)
# 对迭代器进行迭代
for result in it:
    print(result.group(),end=' < ')
    # 获取每一个迭代结果中组的所有的值
    groups = result.groups()
    # 对分组进行迭代
    for i in groups:
        print(i,end = ' ')
    print('>')
