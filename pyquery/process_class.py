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
li.addClass('myitem')
print(li)
li.removeClass('item1')
print(li)
li.removeClass('item2 item3')
print(li)
li.addClass('class1 class2')
print(li)
