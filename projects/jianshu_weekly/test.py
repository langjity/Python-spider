from lxml import etree
import requests
import re
import json
import csv
import os


header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'cookie':'__yadk_uid=xeqG3EJDiKBRfxVO3j2WeLKEUSNMutrB; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fp%2F05ababcf9dd3; read_mode=day; default_font=font2; locale=zh-CN; remember_user_token=W1sxMzYxNDI1OF0sIiQyYSQxMSRWWDhUU0JKOU5oZDZtYjhoblMwclYuIiwiMTU1Mjk4MDMyMy40MDEzNzk4Il0%3D--9e77e2fd513ae03aa8f2d04d3631086dc3edc825; _m7e_session_core=880645e1a3b657e5f8b86e78ebb8adae; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1552980203,1552980323,1552980336,1553048205; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2213614258%22%2C%22%24device_id%22%3A%22169338b879465f-05e36cc0827c6-36657105-3686400-169338b8795759%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22not-signed-in-reply-button%22%7D%2C%22first_id%22%3A%22169338b879465f-05e36cc0827c6-36657105-3686400-169338b8795759%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1553062769'
}
def get_urls(url):
    html = requests.get(url,headers=header)

    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    result = []
    for info in infos:
        article_url_part = info.xpath('div/a/@href')[0]
        result.append("https://www.jianshu.com" + article_url_part)
    return result

def get_info(url):
    pass

url_list = get_urls("https://www.jianshu.com/trending/weekly?page=1")
#https://www.jianshu.com/p/c925fc97bfc8'
print(url_list[0])

