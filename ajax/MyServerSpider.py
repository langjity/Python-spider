import requests
import json
from lxml import etree
result = requests.get('http://localhost:1234/data')
text = result.text.encode('utf-8').decode('unicode-escape')

print(text)
data = json.loads(text)
print('个数：',len(data))
for value in data:
    print(value['name'])


