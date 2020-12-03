import requests
import urllib
import lxml.html
import time
bqg_url="https://www.biquge.com/"      #用来衔接网址
url="https://www.biquge.com/28_28334/"
chapter_url=[]
chapter_url_list1=[]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Chrome/60.0.3100.0 Safari/537.36'
    } 
request= urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(request)
html=lxml.html.parse(response)
hrefs=html.xpath('//*[@id="list"]/dl/dd[*]/a/text()')
chapter_url_list=html.xpath('//*[@id="list"]/dl/dd[*]/a/@href')    #得到类似这种的列表[/28_28334/1558940.html , /28_28334/1558940.html ......]                     
title=hrefs[12:]
for chapter_url in chapter_url_list[12:]:
    chapter_url_list1.append(urllib.parse.urljoin(bqg_url,chapter_url))      #每个网址衔接网络地址，使其可用

def read_chapter(url):          
    request1= urllib.request.Request(url=url, headers=headers)
    response1=urllib.request.urlopen(request1)
    html1=lxml.html.parse(response1)
    name=html1.xpath('//*[@class="bookname"]/h1/text()')[0]       #找到标题
    content=[]
    contents=html1.xpath('//*[@id="content"]/text()')     #找到内容列表
    for i in contents:
        content+="\n\n"+"       "+i.strip()      #增添内容的格式
    content = "".join(content)           #列表变为字符串
    content=content.replace("ｗWw。QВ5.ｃｏМ//", "")
    content=content.replace("最新全本：、、、、、、、、、、", "")         #去掉内容中广告
    with open('C:\\Users\\admin\\Desktop\\code\\water_margin\\水浒传\\' +name+'.txt','w+') as f:
        f.write(content.strip())                    #创建txt
        print(name+'  下载成功')

if __name__ == "__main__":
    for x in chapter_url_list1:    #遍历每个url
        time.sleep(10)
        read_chapter(x)

   
