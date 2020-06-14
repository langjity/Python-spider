from pyquery import PyQuery as pq
import requests
import time
import xlwt
def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'cookie':'请按书中描述换上自己的cookie请求头字段值'}
        result = requests.get(url,headers=headers)
        if result.status_code == 200:
            # 这样会乱码print(result.text)
            html = result.content
            html_doc = str(html, 'utf-8')
            return html_doc
        return None
    except Exception:
        return None

# 产生器
def parse_one_page(html):
    doc = pq(html)
    ul = doc('.gl-warp.clearfix')
    liList = ul('.gl-item')

    for li in liList.items():
        product = li('div > div.p-name.p-name-type-2 > a > em')[0].text

        if product == None:  # 京东精选
            product = li(' div > div.p-name.p-name-type-2 > a').attr('title')

        price = li('div > div.p-price > strong > i').text()
        seller = li('div > div.p-shop > span > a').text()
        yield {
            'product':product,
            'price':price,
            'seller':seller
        }


if __name__ == '__main__':
    urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&psort=3&cid2=653&cid3=655&page={}&s=121&click=0'.format(str(i)) for i in range(1,8,2)]
    header = ['排名','产品', '价格', '卖家']
    book = xlwt.Workbook(encoding='utf-8')
    sheet_all = book.add_sheet('所有手机销量排名')
    sheel_apple = book.add_sheet('Apple手机销量排名')
    sheel_huawei = book.add_sheet('华为手机销量排名')
    sheel_xiaomi = book.add_sheet('小米手机销量排名')
    for h in range(len(header)):
        sheet_all.write(0, h, header[h])
        sheel_apple.write(0, h, header[h])
        sheel_huawei.write(0, h, header[h])
        sheel_xiaomi.write(0, h, header[h])
    i = 1
    apple_i = 1
    huawei_i = 1
    xiaom_i = 1
    for url in urls:
        mobile_infos = parse_one_page(get_one_page(url))
        for mobile_info in mobile_infos:
            print(mobile_info)
            sheet_all.write(i, 0, str(i))
            sheet_all.write(i, 1, mobile_info['product'])
            sheet_all.write(i, 2, mobile_info['price'])
            sheet_all.write(i, 3, mobile_info['seller'])
            if mobile_info['product'].lower().find('apple') != -1:
                sheel_apple.write(apple_i, 0, str(apple_i))
                sheel_apple.write(apple_i, 1, mobile_info['product'])
                sheel_apple.write(apple_i, 2, mobile_info['price'])
                sheel_apple.write(apple_i, 3, mobile_info['seller'])
                apple_i += 1
            if mobile_info['product'].lower().find('华为') != -1:
                sheel_huawei.write(huawei_i, 0, str(huawei_i))
                sheel_huawei.write(huawei_i, 1, mobile_info['product'])
                sheel_huawei.write(huawei_i, 2, mobile_info['price'])
                sheel_huawei.write(huawei_i, 3, mobile_info['seller'])
                huawei_i += 1
            if mobile_info['product'].lower().find('小米') != -1:
                sheel_xiaomi.write(xiaom_i, 0, str(xiaom_i))
                sheel_xiaomi.write(xiaom_i, 1, mobile_info['product'])
                sheel_xiaomi.write(xiaom_i, 2, mobile_info['price'])
                sheel_xiaomi.write(xiaom_i, 3, mobile_info['seller'])
                xiaom_i += 1
            time.sleep(0.1)
            i += 1

    book.save('mobile_rank.xls')