import requests
import re
import json
import csv
import os

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',

}

fetch_comment_count = 15
proxies = {
    "https": "https://27.220.121.173:49508",
}
index = 0
page_index = 0
flag = True
while flag:
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv733&productId=12417265&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(page_index)
    page_index += 1
    html = requests.get(url, headers=header) # ,proxies=proxies
    text = str(html.content, encoding='iso-8859-1')

    leftIndex = text.find('{')
    rightIndex = text.rfind('}')
    json_str = text.replace('fetchJSON_comment98vv733(', '')
    json_str = json_str.replace(")", '')
    json_str = json_str.replace("true", '"true"')
    json_str = json_str.replace("false", '"false"')
    json_str = json_str.replace("null", '"null"')
    json_str = json_str.replace(";", '')
    json_obj = json.loads(json_str)
    for i in range(0,len(json_obj['comments'])):
        try:
            comment = json_obj['comments'][i]['content'].encode(encoding='iso-8859-1').decode('GB18030')
            if comment != '此用户未填写评价内容':
                print('<',index + 1,'>',comment)
                creationTime = json_obj['comments'][i]['creationTime']
                nickname = json_obj['comments'][i]['nickname'].encode(encoding='iso-8859-1').decode('GB18030')
                print(creationTime)
                print(nickname)
                print('----------------')
                index += 1

        except:
            pass
        if index == fetch_comment_count:
            flag = False
            break



