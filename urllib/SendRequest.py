import urllib.request

response=urllib.request.urlopen('https://www.jd.com')
print('response的类型：',type(response))
print('status:',response.status,' msg:',response.msg,' version:', response.version)
print('headers:',response.getheaders())
print('headers.Content-Type',response.getheader('Content-Type'))
print(response.read().decode('utf-8'))

