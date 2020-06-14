from bs4 import BeautifulSoup

html = '''
<html>
    <head><title>这是一个演示页面</title></head>
    <body>
        <a href='a.html'>第一页</a>
        <p>
        <a href='b.html'>第二页</a>
    </body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
print('<' + soup.title.string + '>')
print('[' + soup.a["href"]+ ']')
print(soup.prettify())
