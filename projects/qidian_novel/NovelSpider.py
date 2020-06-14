import xlwt
import requests
from lxml import etree
import time


def getOnePage(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for info in infos:
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]

        yield {
          'title': info.xpath('div[2]/h4/a/text()')[0],
          'author': info.xpath('div[2]/p[1]/a[1]/text()')[0],
           'style': style_1+'·'+style_2,
          'complete':info.xpath('div[2]/p[1]/span/text()')[0],
           'introduce':info.xpath('div[2]/p[2]/text()')[0].strip(),

        }




header = ['标题','作者','类型','完成度','介绍']
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('novels')
for h in range(len(header)):
    sheet.write(0, h, header[h])

urls = ['https://www.qidian.com/all/?page={}'.format(str(i)) for i in range(1,10)]
i = 1
for url in urls:
    novels = getOnePage(url)
    for novel in novels:
        print(novel)
        time.sleep(0.1)
        sheet.write(i, 0, novel['title'])
        sheet.write(i, 1, novel['author'])
        sheet.write(i, 2, novel['style'])
        sheet.write(i, 3, novel['complete'])
        sheet.write(i, 4, novel['introduce'])


        i += 1

book.save('novels.xls')
