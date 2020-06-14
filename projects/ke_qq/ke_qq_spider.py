import requests
from pyquery import PyQuery
import os
import sqlite3
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

db_path = 'data.sqlite'
def save_to_sqlite(data):

    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        # 获取sqlite3.Cursor对象
        c = conn.cursor()
        # 创建persons表
        c.execute('''CREATE TABLE course_list
          (keyword CHAR(50)  NOT NULL,
          course_name   CHAR(100)   NOT NULL,
          education_service   CHAR(50)  NOT NULL,
          price        REAL,
          sales     INT);''')

        conn.commit()
        # 关闭数据库连接
        conn.close()
        print('创建数据库成功')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    #   c.executemany('INSERT INTO t_goods_list values (?,?,?,?,?,?,?,?,?)', goods_list)
    # 下面的4条语句向persons表中插入4条记录
    c.executemany ('INSERT INTO course_list VALUES(?,?,?,?,?)',data)
    conn.commit()
    print('保存数据成功')

# https://ke.qq.com/course/list/python?tuin=a22a65ce
def get_course_list(keyword):
    data = requests.get('https://ke.qq.com/course/list/{}?price_min=1'.format(keyword), headers=headers)
    doc = PyQuery(data.text)
    # 必须使用下面的CSS选择器，因为在代码中有多个class属性值为course-card-list的ul节点，我们只取第1个ul节点
    ul = doc('div.market-bd.market-bd-6.course-list.course-card-list-multi-wrap.js-course-list > ul')
    li_list = ul('li')
    data = []

    for li in li_list.items():
        record = []
        course_name = li('h4 > a').text()
        education_service = li('div.item-line.item-line--middle > span.item-source > a').text()
        price = li('div.item-line.item-line--bottom > span.line-cell.item-price').text()[1:]
        sales = li('div.item-line.item-line--middle > span.line-cell.item-user').text()[:-3]
        record.append(keyword)
        record.append(course_name)
        record.append(education_service)
        record.append(price)
        record.append(sales)
        data.append((record))
        print(record)
    save_to_sqlite(data)



if __name__ == '__main__':
    keyword  = input('请输入关键字：')
    get_course_list(keyword)

