from mitmproxy import ctx
def request(flow):
    print(type(flow.request))
    flow.request.headers['User-Agent'] = 'log proxy'
    ctx.log.error(str(flow.request.headers))
    ctx.log.warn(str(flow.request.headers))
    ctx.log.info(str(flow.request.headers))