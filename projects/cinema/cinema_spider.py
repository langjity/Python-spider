import json
from urllib3 import *

import re
import time

disable_warnings()
http = PoolManager()
def getOnePage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        response = http.request('GET', url, headers=headers)

        data = response.data.decode('utf-8')

        if response.status == 200:
            return data
        return None
    except Exception:
        return None


def parseOnePage(html):
    # re.S：.的作用扩展到整个字符串，包括\n，默认.只针对一行
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def save(content):
    with open('board.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def getBoard(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = getOnePage(url)

    for item in parseOnePage(html):
        print(item)
        save(item)



for i in range(10):
    getBoard(offset=i * 10)
    time.sleep(1)
