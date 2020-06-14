from requests import exceptions,get
import urllib3
try:
    response = get('https://localhost')
    print(response.status_code)
except exceptions.SSLError as e:
    print(e.args[0])


try:
    response = get('https://localhost',verify=False)
    print(response.status_code)
except exceptions.SSLError as e:
    print(e.args[0])

try:
    urllib3.disable_warnings()
    response = get('https://localhost',verify=False)
    print(response.status_code)
except exceptions.SSLError as e:
    print(e.args[0])