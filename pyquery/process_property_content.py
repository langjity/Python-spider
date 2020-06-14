from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1" >
        <li class="item1 item2 item3" >谷歌</li>
        <li class="item1 item2">微软</li>
    </ul>

</div>
'''

doc = pq(html)
li = doc('.item1.item2')

print(li)
print(li.text())
print(li.html())
print('------------------')
li.attr('id','list')
li.attr('class','myitem1,myitem2')
print(li)
li.removeAttr('id')
li.removeAttr('class')
print(li)

li.text('列表')
print(li)
li.text('\n<a href="https://www.google.com"/>\n')
print(li)
li.html('\n<a href="https://www.google.com"/>\n')
print(li)
print(li.text())
print(li.html())