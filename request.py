import requests
url = 'https://httpbin.org/get'
param = {
    'name':'james',
    'password':'mike'
}
response_ = requests.get(url,param)
response_json = response_.json()

del response_json['origin']
print(response_json)