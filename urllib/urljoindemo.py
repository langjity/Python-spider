from urllib.parse import urljoin
# 输出https://www.jd.com/index.html
print(urljoin('https://www.jd.com','index.html'))
# 输出https://www.taobao.com
print(urljoin('https://www.jd.com','https://www.taobao.com'))
# 输出https://www.taobao.com/index.html
print(urljoin('https://www.jd.com/index.html','https://www.taobao.com/index.html'))
# 输出https://www.jd.com/index.php?name=Bill&age=30
print(urljoin('https://www.jd.com/index.php','?name=Bill&age=30'))
# 输出https://www.jd.com/index.php?name=Bill
print(urljoin('https://www.jd.com/index.php?value=123','?name=Bill'))