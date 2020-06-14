function main(splash,args)
    local result = {}
    splash:go("https://www.jd.com")
    splash:wait(0.5)
    result["png1"] = splash:png()
    local timer = splash:call_later(function()
        result["png2"] = splash:png()
    end,2)

    splash:wait(3.0)
    return result
end