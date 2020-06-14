from urllib import request,error
try:
    response = request.urlopen('http://www.jd123.com/test.html')
except error.URLError as e:
    print(e.reason)
try:
    response = request.urlopen('https://geekori.com/abc.html')
except error.URLError as e:
    print(e.reason)
try:
    response = request.urlopen('https://geekori123.com/abc.html')
except error.URLError as e:
    print(e.reason)
try:
    response = request.urlopen('https://bbbccc.com',timeout=2)
except error.URLError as e:
    print(e.reason)