from pyquery import PyQuery as pq
from lxml import etree

doc = pq(filename='test.html')
result = doc('.list1')
aList = result.find('a')
print(type(aList))
for a in aList:
    print(str(etree.tostring(a,pretty_print=True,encoding='utf-8'),'utf-8'))


print('------------------')
result = doc('.item')
aList = result.children('a')

for a in aList:
    print(str(etree.tostring(a,pretty_print=True,encoding='utf-8'),'utf-8'))



