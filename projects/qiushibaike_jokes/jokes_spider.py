import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

jokeLists = []

def verifySex(class_name):
  if class_name == 'womenIcon':
      return '女'
  else:
      return  '男'

def getJoke(url):
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
    sexs = re.findall('<div class="articleGender (.*?)">',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)

    for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        info = {
            'id':id,
            'level':level,
            'sex':verifySex(sex),
            'content':content,
            'laugh':laugh,
            'comment':comment
        }
        jokeLists.append(info)


urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,31)]
for url in urls:
    getJoke(url)
for joke in jokeLists:
    f = open('./jokes.txt','a+')
    try:
        f.write(joke['id']+'\n')
        f.write(joke['level'] + '\n')
        f.write(joke['sex'] + '\n')
        f.write(joke['content'] + '\n')
        f.write(joke['laugh'] + '\n')
        f.write(joke['comment'] + '\n\n')
        f.close()
    except UnicodeEncodeError:
        pass
