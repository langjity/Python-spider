from urllib.parse import parse_qs,parse_qsl

query = 'name=王军&age=35'
# 输出{'name': ['王军'], 'age': ['35']}
print(parse_qs(query))