import http.cookiejar,urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print('------http://www.baidu.com--------')
for item in cookie:
    print(item.name + '=' + item.value)
print('------http://127.0.0.1:5000/writeCookie--------')
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://127.0.0.1:5000/writeCookie')
for item in cookie:
    print(item.name + '=' + item.value)
