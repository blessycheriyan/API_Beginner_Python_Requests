import re
import requests
url = 'https://httpbin.org/status/404'

response_ = requests.post(url)

if response_.status_code == requests.codes.NOT_FOUND:
    print('Not Found')
else:
    print('found')