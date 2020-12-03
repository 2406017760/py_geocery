import urllib
import requests
import lxml.html
import re
from fake_useragent import UserAgent
import random

url='http://202.200.48.24:8900/home'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control':' max-age=0',
    'Cookie': 'login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYpuUwephr8wChTwVs2E7M5GWpVJ7B1HmaPrAAbSWs5s%252FRkDbV0HYk5%252FIbfTVfFYKB0GpePFlk4qvreFAcz8givssP7szNobtyElRCbzlEikZzeJwHDAPndheMFC0NVi%252F9VJUALwthZhipiHgdP1CyjhGV0%252F6YLTl4yGdwr3nUfi9tNPybQF0QP0ax93s1D7%252FftCrWbgiCxa%252FWVe0q3SHxoPXbDkDlf22kheoWuVYOXRX; _csrf=a6b833c7973c15e7f470d7e51dd4ac92d063a67f57bdf44b8e1c6bad09b07803a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22ZQJTFy8iAP8RerIq5dRlPplM9vkVMfIU%22%3B%7D; PHPSESSID=rsk30217m7kqd8l545ep017eu2',
    'Host': '202.200.48.24:8900',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    } 
request= urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(request)
html=lxml.html.parse(response)
hrefs=html.xpath('//*[@id="w5-container"]/table/tbody/tr[*]/td[5]/button[2]/text()')
y=0
for i in hrefs:
    href=re.findall(r"\-?\d+\.?\d*",i)
    x="".join(href)
    x=float(x)
    if x<0:
        x=0
    y=x+y
print("剩余流量为：%.2fG" %y)