function main(splash,args)
    local get_a_count = splash:jsfunc([[

    function() {
        var body = document.body;
        var a_list = body.getElementsByTagName('a');
        return a_list.length;
    }
    ]])
    splash:go("https://www.jd.com")
    return ("These are %s a node"):format(get_a_count())
end