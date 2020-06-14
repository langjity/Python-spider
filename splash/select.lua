function main(splash)
    splash:go("https://www.jd.com")
    input = splash:select('#key')
    input:send_text("Python从菜鸟到高手")
    splash:wait(2)
    return splash:png()
end