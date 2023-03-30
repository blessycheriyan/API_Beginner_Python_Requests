import requests
url = 'https://httpbin.org/delay/3'

   
response_ = requests.get(url,timeout=5)
print(response_)