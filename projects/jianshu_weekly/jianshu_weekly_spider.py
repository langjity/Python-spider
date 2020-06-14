from lxml import etree
import requests
import re
import json
import csv
import os


header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

def get_url(url):
    html = requests.get(url,headers=header)
    selector = etree.HTML(html.text)
    print(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        article_url_part = info.xpath('div/a/@href')[0]
        get_info(article_url_part)
def save_csv(info):
    fieldnames = []
    for key in info:
        fieldnames.append(key)
    if os.path.exists('./weekly.csv'):
        f = open('./weekly.csv', 'a+', encoding='utf-8')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    else:
        f = open('./weekly.csv', 'w', encoding='utf-8')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    writer.writerow(info)


def get_info(url):
    article_url = 'http://www.jianshu.com/' + url
    result = requests.get(article_url,headers=header)
    selector = etree.HTML(result.text)
    print(result.text)
    author = selector.xpath('//span[@class="name"]/a/text()')[0]
    article = selector.xpath('//h1[@class="title"]/text()')[0]
    date = selector.xpath('//span[@class="publish-time"]/text()')[0]
    word = selector.xpath('//span[@class="wordage"]/text()')[0]
    view = re.findall('"views_count":(.*?),',result.text,re.S)[0]
    comment = re.findall('"comments_count":(.*?),',result.text,re.S)[0]
    like = re.findall('"likes_count":(.*?),',result.text,re.S)[0]
    id = re.findall('{"id":(.*?),',result.text,re.S)[0]
    gain_url = 'http://www.jianshu.com/notes/{}/rewards?count=20'.format(id)

    result = requests.get(gain_url,headers=header)
    json_data = json.loads(result.text)
    gain = json_data['rewards_count']

    include_list = []
    include_urls = ['http://www.jianshu.com/notes/{}/included_collections?page={}'.format(id,str(i)) for i in range(1,10)]
    for include_url in include_urls:
        html = requests.get(include_url,headers=header)
        json_data = json.loads(html.text)

        includes = json_data['collections']
        if len(includes) == 0:
            pass
        else:
            for include in includes:
                include_title = include['title']
                include_list.append(include_title)
    info ={
        'author':author,
        'article':article,
        'date':date,
        'word':word,
        'view':view,
        'comment':comment,
        'like':like,
        'gain':gain,
        'include':include_list
    }
    print(info)
    save_csv(info)

if __name__ == '__main__':
    urls = ['http://www.jianshu.com/trending/weekly?page={}'.format(str(i)) for i in range(0, 11)]
    print(urls)
   # for url in urls:
    #    get_url(url)

