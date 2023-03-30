import requests
url = 'https://httpbin.org/post'
payload = {
    'name':'james',
    'password':'mike'
}
response_ = requests.post(url,data = payload)
response_json = response_.json()

del response_json['origin']
print(response_json)