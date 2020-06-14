from lxml import *
from lxml import etree
import requests
import json

def getOnePage(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None

def parseOnePage(html):
    selector = etree.HTML(html)
    items = selector.xpath('//tr[@class="item"]')
    for item in items:
        book_infos = item.xpath('td/p/text()')[0]
        yield {
            'name' :item.xpath('td/div/a/@title')[0],
            'url' :item.xpath('td/div/a/@href')[0],
            'author':book_infos.split('/')[0],
            'publisher':book_infos.split('/')[-3],
            'date': book_infos.split('/')[-2],
            'price': book_infos.split('/')[-1]
        }
def save(content):
    with open('top250books.txt', 'at', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
def getTop250(url):
    html = getOnePage(url)
    for item in parseOnePage(html):
        print(item)
        save(item)
urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]

for url in urls:
    getTop250(url)

