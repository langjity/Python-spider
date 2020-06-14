import requests
url = 'http://localhost:8050/render.png?url=https://www.jd.com&width=800&height=500'
response = requests.get(url)
with open('jd.png','wb') as f:
    f.write(response.content)