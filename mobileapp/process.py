def request(flow):
    print(type(flow))
    flow.request.headers['User-Agent'] = 'This is a proxy.'
    print('下面输出的是HTTP请求头：')
    print(flow.request.headers)