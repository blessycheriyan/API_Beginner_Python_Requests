import requests
url = 'https://httpbin.org/get'

proxies = {
    'http':'123.45.66',
    'http':'123.45.90',
    
}
   
response_ = requests.get(url, proxies=proxies)
print(response_.content)