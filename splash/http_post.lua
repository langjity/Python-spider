function main(splash,args)
    local treat = require("treat")
    local json = require("json")
    local response = splash:http_post{"http://httpbin.org/post",
         body = json.encode({name="Mike",age=30,salary=1234.5}),
         headers = {["content-type"] = "application/json"}
    }

    return {
        html = treat.as_string(response.body),
        url = response.url,
        status = response.status
    }
end