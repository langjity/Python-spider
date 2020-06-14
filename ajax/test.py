import requests
from lxml import etree
result = requests.get('http://localhost:1234')
tree = etree.HTML(result.text)
print(tree.xpath('//*[@id="video_list"]/li[2]')[0].text)
print(tree.xpath('//*[@id="video_list"]/li[6]')[0].text)

