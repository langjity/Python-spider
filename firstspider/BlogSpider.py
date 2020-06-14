# 编写第一个网络爬虫
from urllib3 import *
from re import *
http = PoolManager()
disable_warnings()

def download(url):
    result = http.request('GET', url)
    htmlStr = result.data.decode('utf-8')
    return htmlStr
def analyse(htmlStr):

    aList = findall('<a[^>]*titlelnk[^>]*>[^<]*</a>',htmlStr)
    result = []
    for a in aList:
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]', a)
        if g != None:
            url = g.group(1)

        index1 = a.find(">")
        index2 = a.rfind("<")
        title = a[index1 + 1:index2]
        d = {}
        d['url'] = url
        d['title'] = title
        result.append(d)
    return result

def crawler(url):
    html = download(url)
    blogList = analyse(html)
    for blog in blogList:
        print("title:",blog["title"])
        print("url:",blog["url"])


crawler('https://www.cnblogs.com')