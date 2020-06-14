import json
import os
import sqlite3
from mitmproxy import ctx



db_path = 'igetget.sqlite'

if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    # 获取sqlite3.Cursor对象
    c = conn.cursor()
    # 创建persons表
    c.execute('''CREATE TABLE course_list
      (
      name CHAR(50),
      intro CHAR(50)  ,
      lecturer_name   CHAR(100)  ,
      lecturer_title   CHAR(50) ,
      price       INT,
      phase_num     INT,
      learn_user_count INT
      );''')

    conn.commit()
    # 关闭数据库连接
    conn.close()
    print('创建数据库成功')
conn = sqlite3.connect(db_path)
c = conn.cursor()

def response(flow):

    url = 'https://entree.igetget.com/bauhinia/h5/college/course'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        courses = data.get('c').get('list')
        for course in courses:
            data = [
                 course.get('name'),
                course.get('intro'),
                course.get('lecturer_name'),
                course.get('lecturer_title'),
                course.get('price'),
                course.get('phase_num'),
                course.get('learn_user_count')

            ]
            ctx.log.info(str(data))

            c.execute('INSERT INTO course_list VALUES(?,?,?,?,?,?,?)', data)
            conn.commit()
