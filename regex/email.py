import re
# 匹配Email的正在表达式
email = '[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}'
result = re.findall(email, 'lining@geekori.com')
# 运行结果：['lining@geekori.com']
print(result)
result = re.findall(email, 'abcdefg@aa')
# “@”后面不是域名形式，匹配失败。运行结果：[]
print(result)
result = re.findall(email, '我的email是lining@geekori.com，不是bill@geekori.cn，请确认输入的Email是否正确')
# 运行结果：['lining@geekori.com', 'bill@geekori.cn']
print(result)


# 匹配IPV4的正则表达式
ipv4 = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
result = re.findall(ipv4, '这是我的IP地址：33.12.54.34，你的IP地址是100.32.53.13吗')
# 运行结果：['33.12.54.34', '100.32.53.13']
print(result)
# 匹配Url的正则表达式
url = 'https?:/{2}\w.+'
url1 = 'https://geekori.com'
url2 = 'ftp://geekori.com'
# 运行结果：<_sre.SRE_Match object; span=(0, 19), match='https://geekori.com'>
print(re.match(url,url1))
# 运行结果：None
print(re.match(url,url2))
