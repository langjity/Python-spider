from lxml import etree

parser = etree.HTMLParser()
html   = etree.parse('demo.html', parser)
nodes = html.xpath('//a[@href="https://geekori.com"]')
print('共',len(nodes),'个节点')

for i  in range(0,len(nodes)):
    print(nodes[i].text)


nodes = html.xpath('//a[contains(@href,"www")]')
print('共',len(nodes),'个节点')

for i  in range(0,len(nodes)):
    print(nodes[i].text)

urls = html.xpath('//a[contains(@href,"www")]/@href')

for i  in range(0,len(urls)):
    print(urls[i])





