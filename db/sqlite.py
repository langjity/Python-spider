import sqlite3
import os

dbPath = 'data.sqlite'
# 只有data.sqlite文件不存在时才创建该文件
if not os.path.exists(dbPath):
    # 创建SQLite数据库
    conn = sqlite3.connect(dbPath)
    # 获取sqlite3.Cursor对象
    c = conn.cursor()
    # 创建persons表
    c.execute('''CREATE TABLE persons
     (id INT PRIMARY KEY     NOT NULL,
      name           TEXT    NOT NULL,
      age            INT     NOT NULL,
      address        CHAR(50),
      salary         REAL);''')

    # 修改数据库后必须调用commit方法提交才能生效
    conn.commit()
    # 关闭数据库连接
    conn.close()
    print('创建数据库成功')



conn = sqlite3.connect(dbPath)
c = conn.cursor()
# 删除persons表中的所有数据
c.execute('delete from persons')
# 下面的4条语句向persons表中插入4条记录
c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

c.execute("INSERT INTO persons (id,name,age,address,salary) \
VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
# 必须提交修改才能生效
conn.commit()

print('插入数据成功')
# 查询persons表中的所有记录，并按age升序排列
persons = c.execute("select name,age,address,salary from persons order by age")
print(type(persons))
result = []
# 将sqlite3.Cursor对象中的数据转换为列表形式
for person in persons:
    value = {}
    value['name'] = person[0]
    value['age'] = person[1]
    value['address'] = person[2]
    result.append(value)
conn.close()
print(type(result))
# 输出查询结果
print(result)

import json
# 将查询结果转换为字符串形式，如果要将数据通过网络传输，就需要首先转换为字符串形式才能传输
resultStr = json.dumps(result)
print(type(resultStr))
print(resultStr)
