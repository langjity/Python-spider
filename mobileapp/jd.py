import requests

data = '''
text选项卡中的内容
'''
headers = {
  "Host":"api.m.jd.com",
   "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": 'Cookie数据',
   "User-Agent":"JD4iPhone/165234 (iPhone; iOS 12.2; Scale/3.00)"
}
response = requests.post('http://api.m.jd.com/client.action?functionId=tip',data=data,headers=headers)
print(response.text)

