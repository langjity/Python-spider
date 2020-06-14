function main(splash,args)
    local ok,reason = splash:go{"http://httpbin.org/post",http_method="POST",body="name=Bill"}
    if ok then
        return {
            html = splash:html(),
            har = splash:har()
        }
    end

end