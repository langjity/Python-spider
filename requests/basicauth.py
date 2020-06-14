import requests

from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000',auth=HTTPBasicAuth('bill','1234'))
print(r.status_code)
print(r.text)