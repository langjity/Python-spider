from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup演示</title>
</head>
<body>
<div>
    <ul>
        <li class="item1"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.head)
print(type(soup.head))
head = soup.head
print(head.title.string)
print(soup.body.div.ul.li.a['href'])



