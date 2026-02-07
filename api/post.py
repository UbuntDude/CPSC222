from urllib.parse import urlencode
from urllib.request import Request, urlopen

url= 'http://127.0.0.1:3000/'
post_fields={'u':'me','p':'password'}

request=Request(url, urlencode(post_fields).encode())
with urlopen(request) as response:
    json=response.read().decode()
print(json)
