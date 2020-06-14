function main(splash,args)
    splash:autoload([[
        function get_document_title() {
            return document.title;
        }

        function get_div_count() {
            var body = document.body;
            var div_list = body.getElementsByTagName('div');
            return div_list.length;
        }
    ]])
    splash:autoload{url="https://code.jquery.com/jquery-3.3.0.min.js"}

    splash:go("https://www.jd.com")
    local version = splash:evaljs("$.fn.jquery")
    local a_count = splash:evaljs("$('a').length;")
    return {
        title=splash:evaljs("get_document_title()"),
        div_count = splash:evaljs("get_div_count()"),
        jquery_version = version,
        a_count = a_count

    }
end