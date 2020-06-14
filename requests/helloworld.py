import requests
r = requests.get('https://www.taobao.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.cookies)
print(r.text)
