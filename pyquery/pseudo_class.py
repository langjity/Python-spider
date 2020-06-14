import pyquery
from pyquery import PyQuery as pq
html = '''
<div>
    <ul>
        <li class="item1" ><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城（https://www.jd.com）</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>              

    </ul>

</div>

'''

doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(3)')
print(li)
li = doc('li:lt(2)')
print(li)
li = doc('li:gt(3)')
print(li)

li = doc('li:nth-child(2n+1)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(com)')
print(li)
all = doc(':contains(com)')
print(len(all))
for t in all:
    print(t.tag, end=' ')

