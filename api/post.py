from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

url= 'http://10.50.19.230:3000/'
final_url='http://httpbin.org/post'
payload={'u':'username','p':'password'}

r=requests.post(final_url,data=payload)
print(r.text)
