import requests
url = 'https://httpbin.org/user-agent'
headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
   
response_ = requests.get(url, headers = headers)

print(response_.text)

