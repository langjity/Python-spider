function main(splash)
    local treat = require('treat')
    splash:go("https://www.jd.com")
    splash:wait(0.5)
    local a_list = splash:select_all('a')
    local results = {}
    for index,a in ipairs(a_list) do
        results[index] = {text = a.node.innerHTML,href=a.node.attributes.href}
    end
    return treat.as_array(results)
end