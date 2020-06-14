from pyquery import PyQuery as pq
from snownlp import SnowNLP
import requests
import threading
import _thread as thread
import datetime
from PyQt5.QtCore import QObject, pyqtSignal,QThread
from urllib.parse import urlparse
from urllib.parse import parse_qs
from database import *
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
class BaseSpider:
    def get_content(url):
        content = requests.get(url, headers=headers)
        if content.status_code == 200:
            return content.text
        return None

class UrlHousing:
    def __init__(self):
        self.urls = []
        self.lock = threading.Lock()
    def get_url(self):
        self.lock.acquire()
        if len(self.urls) == 0:
            self.lock.release()
            return ""
        else:
            url = self.urls[0]
            del self.urls[0]
        self.lock.release()
        return url


class SearchSpider (QThread,BaseSpider):   #继承父类threading.Thread
    sendmsg = pyqtSignal(int,int)
    def __init__(self,name,keyword):
        super(SearchSpider, self).__init__()
        self.name = name
        self.url = 'http://search.dangdang.com/?key={}&act=input'.format(keyword)
        self.keyword = keyword

    def run(self):
        print('<<<<<<<<<<<<<<线程',self.name,'开始运行>>>>>>>>>>>>>>>')
        html = BaseSpider.get_content(self.url)
        doc = pq(html)
        # 获取商品页数
        result1 = doc('#go_sort > div > div.data > span:nth-child(3)')
        result2 = doc('#component_59 > li')
        every_page_goods_number = len(result2)
        try:
            self.sendmsg.emit(int(result1.text()[1:]),every_page_goods_number)
        except Exception as e:
            print(e)
        print('<<<<<<<<<<<<<<线程', self.name, '结束运行>>>>>>>>>>>>>>>')



class GoodsPageSpider (QThread,BaseSpider):

    # page_index：当前抓取的页索引，从1开始
    # get_url：回调函数
    def __init__(self, name, goods_list_spider):
        super(GoodsPageSpider, self).__init__()
        self.name = name
        self.goods_list_spider = goods_list_spider
        self.goods_list = []
    def save_image(self,index,url):
        try:
            if not os.path.exists('images'):
                os.mkdir('images')
            r = requests.get(url)
            # 不加扩展名，自动识别
            filename = str(index).zfill(8)
            with open('images/' + filename, 'wb') as f:
                f.write(r.content)
        except:
            pass

    def run(self):
        print('<<<<<<<<<<<<<<线程', self.name, '开始运行>>>>>>>>>>>>>>>')
        while True:
            url = self.goods_list_spider.get_url()
            if url == "":
                break;

            result = urlparse(url)
            page_index = int(parse_qs(result.query)['page_index'][0])

            html = BaseSpider.get_content(url)
            doc = pq(html)
            liList = doc('#component_59 > li')
            every_page_goods_number = len(liList)
            start_index = every_page_goods_number * (page_index - 1) + 1

            for li in liList.items():
                goods_info = []
                title = li('a.pic').attr.title
                now_price = li('span.search_now_price').text()[1:]
                pre_price = li('span.search_pre_price').text()[1:]
                comment_num = li('a.search_comment_num').text()[:-3]
                publication_date = li('p.search_book_author > span:nth-child(2)').text()[1:]
                publisher = li('p.search_book_author > span:nth-child(3) > a').text()
                image_url = li('a > img').attr['data-original']
                if image_url == None:
                    image_url = li('a > img').attr.src
                goods_url = li('a').attr.href

                goods_info.append(start_index)
                goods_info.append(title)
                goods_info.append(now_price)
                goods_info.append(pre_price)
                goods_info.append(comment_num)
                goods_info.append(publication_date)
                goods_info.append(publisher)
                goods_info.append(image_url)
                goods_info.append(goods_url)
                self.save_image(start_index,image_url)
                self.goods_list.append(goods_info)
                print("线程",self.name,':',goods_info)
                start_index += 1


        print('<<<<<<<<<<<<<<线程线程', self.name, '结束运行>>>>>>>>>>>>>>>')



class GoodsListSpider(QObject,UrlHousing):
    finished = pyqtSignal(float,int)
    def __init__(self,keyword, max_page_index,max_thread_number):
        super(GoodsListSpider, self).__init__()
        self.spiders = []
        self.keyword = keyword
        self.max_page_index = max_page_index
        self.max_thread_number = max_thread_number
        self.urls = ['http://search.dangdang.com/?key={}&act=input&page_index={}'.format(keyword,i) for i in range(1,max_page_index + 1)]

    def run(self):
        self.db = Database()
        self.db.open()
        starttime = datetime.datetime.now()
        for i in range(0,self.max_thread_number):
            spider = GoodsPageSpider("GoodsPageSpider" + str(i + 1),self)
            self.spiders.append(spider)
            spider.start()
        print('共启动了', self.max_thread_number, '个GoodsPageSpider爬虫线程')
        book_number = 0
        for spider in self.spiders:
            spider.wait()
            self.db.insert_goods_list(spider.goods_list)
            book_number += len(spider.goods_list)
        self.db.close()
        endtime = datetime.datetime.now()
        self.finished.emit((endtime - starttime).seconds,book_number)

    def start(self):
        thread.start_new_thread(self.run,())

class GoodsCommentPageSpider (QThread,BaseSpider):

    progress = pyqtSignal(int,int,float)
    # page_index：当前抓取的页索引，从1开始
    # get_url：回调函数
    def __init__(self, thread_id,name, goods_comment_spider):
        super(GoodsCommentPageSpider, self).__init__()
        self.name = name
        self.finished_comment_num = 0
        self.thread_id = thread_id
        self.goods_comment_spider = goods_comment_spider
        self.goods_comment_list = []

    def run(self):
        print('<<<<<<<<<<<<<<线程', self.name, '开始运行>>>>>>>>>>>>>>>')
        while True:

            try:
                url = self.goods_comment_spider.get_url()
                if url == "":
                    break;

                json_str = BaseSpider.get_content(url)
                json_obj = json.loads(json_str)

                html = json_obj['data']['list']['html']
                doc = pq(html)
                comment_items = doc('.comment_items')
                for item in comment_items.items():
                    comment_score = item('em').text()
                    comment_score = comment_score[0:len(comment_score) - 1]

                    describe_detail = item('.describe_detail').text()
                    if describe_detail == "":
                        continue
                    s = SnowNLP(describe_detail)
                    comment_time = item('.starline > span:first-child').text()

                    comment = []
                    comment.append(self.goods_comment_spider.goods_id)
                    comment.append(describe_detail)
                    comment.append(comment_score)
                    comment.append(comment_time)
                    comment.append(s.sentiments)

                    self.goods_comment_list.append(comment)
                    self.finished_comment_num += 1
                    self.progress.emit(self.thread_id,self.finished_comment_num,s.sentiments)


            except:

                pass

        print('<<<<<<<<<<<<<<线程线程', self.name, '结束运行>>>>>>>>>>>>>>>')


class GoodsCommentSpider (QObject,UrlHousing):
    progress = pyqtSignal(int,int,float)
    def __init__(self, name,product_id,goods_id):
        super(GoodsCommentSpider, self).__init__()
        self.spiders = []
        self.name = name
        self.product_id = product_id
        self.MAX_PAGE = 500
        self.MAX_THREAD = 3
        self.goods_id = goods_id
        self.urls = ['http://product.dangdang.com/index.php?r=comment%2Flist&productId={}&categoryPath=01.54.06.19.00.00&mainProductId={}&mediumId=0&pageIndex={}&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0&template=publish'.format(self.product_id,self.product_id,str(i)) for i in range(1,self.MAX_PAGE + 1)]
    def comment_progress(self,thread_id,finished_comment_num,sentiment):
        self.progress.emit(thread_id,finished_comment_num,sentiment)
    def run(self):
        self.db = Database()
        self.db.open(clear_data = False)

        for i in range(0,self.MAX_THREAD):
            spider = GoodsCommentPageSpider(i, "GoodsCommentPageSpider" + str(i + 1),self)
            spider.progress.connect(self.comment_progress)
            self.spiders.append(spider)

            spider.start()
        print('共启动了', self.MAX_THREAD, '个GoodsCommentPageSpider爬虫线程')
        self.db.delete_goods_comment_list(self.goods_id)
        for spider in self.spiders:
            spider.wait()
            self.db.insert_goods_comment_list(spider.goods_comment_list)


        self.db.close()
    def start(self):
        thread.start_new_thread(self.run,())