from urllib.parse import urlparse,urlunparse

result = urlparse('https://search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment')

print('scheme：',result.scheme)
print('netloc：',result.netloc)
print('path：',result.path)
print('params：',result.params)
print('query：',result.query)
print('fragment：',result.fragment)
print('-----------------')
result = urlparse('search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment',scheme='ftp',allow_fragments=False)

print('scheme：',result.scheme)
print('fragment：',result.fragment)

print('----------------')
data = ['https','search.jd.com','Searchprint','world','keyword=Python从菜鸟到高手&enc=utf-8','comment']

print(urlunparse(data))


