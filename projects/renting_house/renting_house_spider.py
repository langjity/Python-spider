from bs4 import BeautifulSoup
import requests
import time
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

def save_house_image(url,name):
    r = requests.get(url)
    name = str.replace(name,'/','')
    with open('images/' + name, 'wb') as f:
        f.write(r.content)

def get_links(url):
    result = requests.get(url,headers=headers)
    soup = BeautifulSoup(result.text,'lxml')
    links = soup.find_all(class_='resule_img_a')

    for link in links:
        href = link["href"]
        house_info = get_info(href)
        print(house_info)
        f.write(json.dumps(house_info,ensure_ascii=False) + '\n')

def get_info(url):
    result = requests.get(url,headers=headers)
    soup = BeautifulSoup(result.text,'lxml')
    div = soup.find(class_='pho_info')
    title = div.h4.em.string
    address = div.p.span.string
    price = soup.find(class_='detail_avgprice').string
    image_url = soup.find(id='curBigImage')['src']
    name = soup.find(class_='lorder_name').string
    member_ico = soup.find(class_='member_boy_ico')
    sex = '男'
    if member_ico == None:
        sex = '女'

    info = {
        'title':title,
        'address':address.strip(),
        'price':price,
        'image_url':image_url,
        'name':name,
        'sex':sex

    }

    save_house_image(image_url, title + ".png")
    return info


if __name__ == '__main__':
    f = open('./houses.txt', 'a+')
    urls = ['http://sy.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,11)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(1)
    f.close()