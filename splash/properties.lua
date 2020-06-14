function main(splash,args)

    local url1 = splash.args.url
    local url2 = args.url

    splash:go("https://www.jd.com")
    --splash.js_enabled = false
    splash:wait(0.5)
    --splash.resource_timeout = 0.1
    --assert(splash:go("https://www.jd.com"))
    local title = splash:evaljs("document.title")

    splash:go("https://www.jd.com")
    png1 = splash.png()
    splash.images_enabled = false
    splash:go("https://www.jd.com")
    splash.scroll_position = {y=500 }

    png2 = splash.png()
    return {
        url1 = url1,
        url2 = url2,
        title = title,
        png1 = png1,
        png2 = png2
    }
end