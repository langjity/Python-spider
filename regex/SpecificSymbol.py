import re
# 匹配'a'、'b'、'c'三个字母按顺序从左到右排列，而且这3个字母都必须至少有1个。
# abc aabc   abbbccc都可以匹配成功
s = 'a+b+c+'
strList = ['abc','aabc','bbabc','aabbbcccxyz']
# 只有'bbabc'无法匹配成功，因为开头没有'a'
for value in strList:
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))

print('--------------')

# 匹配任意3个数字-任意3个小写字母
# 123-abc   433-xyz都可以成功
# 下面采用了两种设置模式字符串的方式
# [a-z]是设置字母之间或关系的简化形式，表示a到z的26个字母可以选择任意一个，相当于“a|b|c|…|z”
#s = '\d\d\d-[a-z][a-z][a-z]'
# {3}表示让前面修饰的特殊字符“\d”重复3次，相当于“\d\d\d”
s = '\d{3}-[a-z]{3}'
strList = ['123-abc','432-xyz','1234-xyz','1-xyzabc','543-xyz^%ab']
# '1234-xyz'和'1-xyzabc'匹配失败
for value in strList:
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))
print('-------------')
# 匹配以a到z的26个字母中的任意一个作为前缀（也可以没有这个前缀），后面是至少1个数字
s = '[a-z]?\d+'
strList = ['1234','a123','ab432','b234abc']
# 'ab432'匹配失败，因为前缀是两个字母
for value in strList:
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))

print('-------------')
# 匹配一个email
email = '\w+@(\w+\.)*\w+\.com'
emailList =['abc@126.com','test@mail.geekori.com','test-abc@geekori.com','abc@geekori.com.cn']
# 'test-abc@geekori.com'匹配失败，因为“test”和“abc”之间有连字符（-）
for value in emailList:
    m = re.match(email,value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,email))
strValue = '我的email是lining@geekori.com，请发邮件到这个邮箱'
# 搜索文本中的email，由于“\w”对中文也匹配，所以下面对email模式字符串进行改进
m = re.search(email, strValue)
print(m)
# 规定“@”前面的部分必须是至少1个字母（大写或小写）和数字，不能是其他字符
email = '[a-zA-Z0-9]+@(\w+\.)*\w+\.com'
m = re.search(email, strValue)
print(m)
