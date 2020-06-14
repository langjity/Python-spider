import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return "世界，你好"
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)

lua = '''
function main(splash)
    splash:go("https://weather.com")
    splash:wait(3)
    return {
        html = splash:html(),
        png = splash:png()
        
    }
end

'''
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
import json
import base64
json_obj = json.loads(response.text)
png_base64 = json_obj['png']
png_bytes = base64.b64decode(png_base64)

with open('weather.png','wb') as f:
    f.write(png_bytes)
