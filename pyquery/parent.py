from pyquery import PyQuery as pq


doc = pq(filename='test.html')
result = doc('.item')
print(result.parent())
print('------------')
print('父节点数：',len(result.parents()))
print(result.parents())
print('父节点数：',len(result.parents('#panel')),'节点名：',result.parents('#panel')[0].tag)