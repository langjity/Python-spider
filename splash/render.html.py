import requests
url = 'http://localhost:8050/render.html?url=https://www.jd.com'
response = requests.get(url)
print(response.text)