from lxml import etree

parser = etree.HTMLParser()
html   = etree.parse('demo.html', parser)
result = html.xpath('//a[@href="https://www.jd.com"]/../@class')
print('class属性 =',result)
result = html.xpath('//a[@href="https://www.jd.com"]/parent::*/@class')
print('class属性 =',result)
