import requests

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=0200015"

response = requests.get(url)

print(response)

print(response.text)

