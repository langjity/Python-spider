from urllib.parse import urlencode,urljoin
params = {
    'name':'王军',
    'country':'China',
    'age':30
}

base_url = 'https://www.google.com?'
#url = base_url + urlencode(params)
url = urljoin(base_url,'?' + urlencode(params))
print(url)