import re
# 进行文本模式匹配，匹配失败，match方法返回None
m = re.match('python','I love python.')
if m is not None:
    print(m.group())
# 运行结果：None
print(m)
# 进行文本模式搜索，搜索成功
m = re.search('python','I love python.')
if m is not None:
    # 运行结果：python
    print(m.group())
# 运行结果：<_sre.SRE_Match object; span=(7, 13), match='python'>
print(m)
