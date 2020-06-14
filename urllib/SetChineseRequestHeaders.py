from urllib import request
from urllib.parse import unquote,urlencode
import base64

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Host':'httpbin.org',
    'Chinese1':urlencode({'name':'李宁'}),

    'MyChinese':base64.b64encode(bytes('这是中文HTTP请求头',encoding='utf-8')),
    'who':'Python Scrapy'
}
dict = {
    'name':'Bill',
    'age':30
}
data = bytes(urlencode(dict),encoding='utf-8')
req = request.Request(url = url,data=data,headers=headers,method="POST")
req.add_header('Chinese2',urlencode({"国籍":"中国"}))
response=request.urlopen(req)

value = response.read().decode('utf-8')
print(value)
import json

responseObj = json.loads(value)

print(unquote(responseObj['headers']['Chinese1']))
print(unquote(responseObj['headers']['Chinese2']))
print(str(base64.b64decode(responseObj['headers']['Mychinese']),'utf-8'))


