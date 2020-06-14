from lxml import etree
import requests
import re
import json
import csv
import os


header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

def get_user_dynamic_state(id, page_index):
    url = "https://www.jianshu.com/users/{}/timeline?page={}".format(id,page_index)
    #print(url)
    html = requests.get(url,headers=header)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        comment_list = info.xpath('div/p/text()')
        if len(comment_list) > 0:
            print(comment_list)


def get_info(id):
    pass

#url_list = get("https://www.jianshu.com/users/05f7232fb407/timeline?max_id=422249265&page=2")
get_user_dynamic_state('05f7232fb407',1)



