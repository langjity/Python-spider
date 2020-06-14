import requests
from urllib.parse import quote
lua = '''

function main(splash,args)

    splash:go("https://search.jd.com/Search?keyword=python&page="..args.page)
    splash:wait(1)
    li_list = splash:select_all('#J_goodsList > ul > li > div > div > a')
    titles = {}
    for _, li in ipairs(li_list) do
      titles[#titles+1] =   li.node.attributes.title;
     
    end

    return {
        titles = titles,
        png = splash:png() 
    }
end
'''

url_list = [('http://localhost:8050/execute?lua_source=' + quote(lua) + '&page={}').format(str(i)) for i in range(1,13,2)]
i = 1
for url in url_list:
    response = requests.get(url)
    import json
    import base64
    json_obj = json.loads(response.text)
    print(json_obj['titles'])
    png_base64 = json_obj['png']
    png_bytes = base64.b64decode(png_base64)
    with open(str(i) + '.png','wb') as f:
        f.write(png_bytes)
    i += 1

