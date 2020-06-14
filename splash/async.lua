function main(splash,args)
    local urls = {"www.baidu.com","www.jd.com","www.microsoft.com" }
    local results = {}
    for index, url in ipairs(urls) do
        local ok,reason = splash:go("https://"..url)
        if ok then
            splash:wait(1)
            results[url] = splash:png()
        end

    end
    return results
end
