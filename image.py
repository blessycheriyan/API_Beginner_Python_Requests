import requests
url = 'https://httpbin.org/image'
headers = {
  "Accept": "image/png"
}
   
response_ = requests.get(url, headers = headers)

with open('myimage1.png','wb') as f:
    f.write(response_.content)
