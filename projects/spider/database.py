import sqlite3
import os

class Database:
    def __init__(self):
        self.db_path = 'goods.sqlite'
    def open(self,clear_data = True):

        if not os.path.exists(self.db_path):
            self.conn = sqlite3.connect(self.db_path)
            c = self.conn.cursor()
            c.execute('''CREATE TABLE t_goods_list
             (id INT PRIMARY KEY     NOT NULL,
              title           TEXT    NOT NULL,
              now_price       REAL     NOT NULL,
              pre_price       REAL    NOT NULL,
              comment_num     INT     NOT NULL,
              publication_date DATE NOT NULL,
              publisher TEXT NOT NULL,
              image_url TEXT,
              goods_url TEXT NOT NULL 
              
              );
             
              ''')
            c.execute('''
                          CREATE TABLE t_goods_comment_list
                                     (goods_id INT    NOT NULL,
                                      detail          TEXT,
                                      score           INT,
                                      time            DATETIME,
                                      sentiment       REAL
                                      );
                          ''', {})
            self.conn.commit()
            # 关闭数据库连接
            print('成功创建数据库')
        else:  # 打开数据库
            self.conn = sqlite3.connect(self.db_path)
            if clear_data:
                c = self.conn.cursor()
                c.execute('''
                  DELETE FROM t_goods_list;
                 ''')

                self.conn.commit()
    # goods_list是一个包含列表（元组）的列表，可以一次性插入多条记录
    def insert_goods_list(self,goods_list):
        c = self.conn.cursor()
        c.executemany('INSERT INTO t_goods_list values (?,?,?,?,?,?,?,?,?)', goods_list)
        self.conn.commit()
    def select_goods_list(self):
        c = self.conn.cursor()
        goods_list = c.execute('SELECT * FROM t_goods_list ORDER BY id')
        result = []
        for goods in goods_list:
            goods_info = {}
            goods_info['title'] = goods[1]
            goods_info['price'] = goods[2]
            goods_info['comment_num'] = goods[4]
            goods_info['publication_date'] = goods[5]
            goods_info['publisher'] = goods[6]
            goods_info['image_url'] = goods[7]
            goods_info['goods_url'] = goods[8]
            result.append(goods_info)
        return result
    def close(self):
        print('数据库已经关闭')
        self.conn.close()


    def insert_goods_comment_list(self,goods_comment_list):
        c = self.conn.cursor()

        c.executemany('INSERT INTO t_goods_comment_list values (?,?,?,?,?)', goods_comment_list)
        self.conn.commit()

    def delete_goods_comment_list(self,goods_id):
        c = self.conn.cursor()
        c.execute('''
                     DELETE FROM t_goods_comment_list WHERE goods_id=?;
                   ''',[goods_id])
        self.conn.commit()
    # 如果goods_id等于-1，表示按月获取所有商品的评论数
    def get_comment_count_list_for_month(self,goods_id = -1):
        c = self.conn.cursor()

        goods_comment_list = c.execute('''
            select * from (
                  select goods_id,substr(time,1,7) as month,count(time) as c from t_goods_comment_list   
                   group by goods_id,substr(time,1,7) ) where goods_id=? and c > 10  order by month 
            ''',[goods_id])

        result = []

        for goods_comment in goods_comment_list:

            goods_comment_info = {}
            goods_comment_info['goods_id'] = goods_comment[0]
            goods_comment_info['month'] = goods_comment[1]
            goods_comment_info['count'] = goods_comment[2]
            result.append(goods_comment_info)
        return result


