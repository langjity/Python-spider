import random
from scrapy import Request

class SimulateUserAgentMiddleware():
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15',
            'Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/64.0'
        ]
    
    def process_request(self, request, spider):
        print(request.headers)
        request.headers['User-Agent'] = random.choice(self.user_agents)
        print(request.headers)
    
    def process_response(self, request, response, spider):
        response.status = 201

        return response


class SpiderMiddleware():

    def process_start_requests(self,start_requests,spider):
        for r in start_requests:
            print(r)
            r.headers['User-Agent'] = "my user-agent"
            yield r
    def process_spider_input(self,response,spider):
        response.status = 202