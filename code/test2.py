import urllib
import requests
url=input("请输入网页(包含http://)：")
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Chrome/60.0.3100.0 Safari/537.36',
    } 
request= urllib.request.Request(url=url, headers=headers)  
response=urllib.request.urlopen(request)
print("网页源码为:\n\n" + response.read().decode('utf-8'))