from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1">
        <li class="item" value1="1234" value2 = "hello world">
            Hello
            123
            <a href="https://geekori.com"> geekori.com</a>
            World
        </li>
        <li class="item1" >
        </li>
    </ul>
    <ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item"  value1="4321" value2 = "世界你好" >
            <a href="https://www.microsoft.com">微软</a>
        </li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
'''

doc = pq(html)
result = doc('.item')
print(type(result))

print('-------获取节点名---------')
print(type(result[0]))
print(result[0].tag)
print(result[1].tag)
print('-------获取属性---------')
print('value1:',result[0].get('value1'))

print('value2:',result.attr('value2'))
print('value2:',result.attr.value2)

print('----------------')
for li in result.items():
    print(type(li))
    print(li.attr.value2)

for li in result:
    print(type(li))
    print(li.get('value2'))
print('--------获取文本--------')
# 获取文本
print(result.text())
print('result.text()的类型：',type(result.text()))
from urllib.parse import quote,unquote

for node in result:
    print(node.text)
print('-------节点HTML代码--------')
from lxml import etree
for node in result:
    print(str(etree.tostring(node, pretty_print=True,encoding='utf-8'),'utf-8'))

print('-------获取节点内部HTML代码---------')
print(result.html())
