import requests

base_url = 'https://ozone.bg'
category = '/laptopi-i-computri/mrejovi/routers/?marka='
brand = 'asus'
url = base_url+category+brand

res = requests.get(url)

print(res.text)[:200]




