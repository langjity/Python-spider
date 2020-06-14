from urllib.parse import quote,unquote
keyword = '李宁'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
url = unquote(url)
print(url)