from lxml import etree

parser = etree.HTMLParser()
text = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>XPath演示</title>
</head>
<body class="item">
<div>
    <ul class="item" >
        <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com">京东商城</a>
                            <value url="https://geekori.com"/>
                            <value url="https://www.google.com"/>
        </li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a>
                          <a href="https://www.tmall.com/">天猫</a></li>
        <li class="item4" value="1234"><a href="https://www.microsoft.com">微软</a></li>
        <li class="item5"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
</html>
'''
html   = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
for value in result:
    print(value.tag, end= ' ')

print()
result = html.xpath('//li[1]/ancestor::*[@class="item"]')
for value in result:
    print(value.tag, end= ' ')


print()
result = html.xpath('//li[4]/attribute::*')
print(result)


result = html.xpath('//li[3]/child::*')
for value in result:
    print(value.get('href'), value.text,end= ' ')
print()

result = html.xpath('//li[2]/descendant::value')
for value in result:
    print(value.get('url'),end= ' ')
print()

result = html.xpath('//li[1]/following::*')
for value in result:
    print(value.tag,end= ' ')
print()

result = html.xpath('//li[1]/following::*[position() > 4]')
for value in result:
    print(value.tag,end= ' ')
print()

result = html.xpath('//li[1]/following-sibling::*')
for value in result:
    print(value.tag,end= ' ')
print()