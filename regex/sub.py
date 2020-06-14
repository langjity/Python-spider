import re
# sub函数第1个参数是模式字符串，第2个参数是要替换的字符串，第3个参数是被替换的字符串
# 匹配'Bill is my son'中的'Bill'，并用'Mike'替换'Bill'
result = re.sub('Bill', 'Mike', 'Bill is my son')
# 运行结果：Mike is my son
print(result)
# 返回替换结果和替换总数
result = re.subn('Bill', 'Mike', 'Bill is my son，I like Bill')
# 运行结果：('Mike is my son，I like Mike', 2)
print(result)
# 运行结果：Mike is my son，I like Mike
print(result[0])
# 运行结果：替换总数 = 2
print('替换总数','=',result[1])
# 使用“\N“形式引用匹配字符串中的分组
result = re.sub('([0-9])([a-z]+)', r'产品编码（\1-\2）','01-1abc,02-2xyz,03-9hgf')
# 运行结果：01-产品编码（1-abc),02-产品编码（2-xyz),03-产品编码（9-hgf)
print(result)
# 该函数返回要替换的字符串
def fun():
    return r'产品编码（\1-\2）'
result = re.subn('([0-9])([a-z]+)', fun(),'01-1abc,02-2xyz,03-9hgf')
# 运行结果：('01-产品编码（1-abc）,02-产品编码（2-xyz）,03-产品编码（9-hgf）', 3)
print(result)
# 运行结果：01-产品编码（1-abc）,02-产品编码（2-xyz）,03-产品编码（9-hgf）
print(result[0])
# 运行结果：替换总数 = 3
print('替换总数','=',result[1])
