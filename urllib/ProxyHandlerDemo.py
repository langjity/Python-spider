from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy_handler = ProxyHandler({
    #'http':'http://103.100.96.174:53281',
    'http':'http://182.86.191.16:24695',
    'https':'https://182.86.191.16:24695'
})

opener = build_opener(proxy_handler)
try:
    #response = opener.open('http://blogjava.net')
    response = opener.open('https://www.jd.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)