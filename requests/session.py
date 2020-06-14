import requests
# 不使用Session
requests.get('http://httpbin.org/cookies/set/name/Bill')
r1 = requests.get('http://httpbin.org/cookies')
print(r1.text)

# 使用Session
session = requests.Session()
session.get('http://httpbin.org/cookies/set/name/Bill')
r2 = session.get('http://httpbin.org/cookies')
print(r2.text)
