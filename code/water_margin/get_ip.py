from fake_useragent import UserAgent
import requests
import urllib.request
import re
import random

def Get_IP():
    headers = {
        'User-Agent': UserAgent().random
    }
    html = urllib.request.Request(url='http://www.xiladaili.com/gaoni/', headers=headers)
    html = urllib.request.urlopen(html).read().decode('utf-8')
    reg = r'<td>(.+?)</td>'
    reg = re.compile(reg)
    pools = re.findall(reg, html)[0:4990:8]
    Random_IP = random.choice(pools)
    return Random_IP

if __name__ == "__main__":
    Get_IP