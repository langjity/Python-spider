from mitmproxy import ctx

def request(flow):
    url = 'https://geekori.com'
    flow.request.url = url