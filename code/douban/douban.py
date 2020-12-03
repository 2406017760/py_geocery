import requests
import urllib
import lxml.html
from fake_useragent import UserAgent
import xlrd
import xlwt
from xlutils.copy import copy
import time

ua = UserAgent()
url="https://movie.douban.com/top250"
headers = {
    'User-Agent':ua.random
    }

def wt():
    request= urllib.request.Request(url=url, headers=headers)
    response=urllib.request.urlopen(request)
    html=lxml.html.parse(response)
    title=html.xpath('//*/div/div[2]/div[1]/a/span[1]/text()')[1:]
    content=html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/p[1]/text()[1]')
    classs=html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/p[1]/text()[2]')
    score=html.xpath('//*[@class="rating_num"]/text()')
    workbook=xlwt.Workbook()
    sheet=workbook.add_sheet('movie_top250',cell_overwrite_ok=True)
    for i in range(0,len(title)):
        sheet.write(i,0,title[i])
        sheet.write(i,1,classs[i].strip())
        sheet.write(i,2,score[i])
        sheet.write(i,3,content[i].strip())
        workbook.save('C:\\Users\\admin\\Desktop\\py.xls')
    print("---------------数据写入成功（1/10）------------")

def catch_other(url):
    request= urllib.request.Request(url=url, headers=headers)
    response=urllib.request.urlopen(request)
    html=lxml.html.parse(response)
    title=html.xpath('//*/div/div[2]/div[1]/a/span[1]/text()')[1:]
    content=html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/p[1]/text()[1]')
    classs=html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/p[1]/text()[2]')
    score=html.xpath('//*[@class="rating_num"]/text()')
    xlsx=xlrd.open_workbook('C:\\Users\\admin\\Desktop\\py.xls')
    workbook=copy(xlsx)
    sheet=xlsx.sheets()[0]
    lie=sheet.nrows-1
    sheet=workbook.get_sheet('movie_top250')
    for i in range(0,len(title)):
        lie=lie+1
        sheet.write(lie,0,title[i])
        sheet.write(lie,1,classs[i].strip())
        sheet.write(lie,2,score[i])
        sheet.write(lie,3,content[i].strip())
    workbook.save('C:\\Users\\admin\\Desktop\\py.xls')


    
if __name__ == "__main__":
    wt()
    url_pr="https://movie.douban.com/top250?start="
    url_end="&filter="
    for x in range(25,226,25):
       url_other=url_pr+str(x)+url_end
       catch_other(url_other)
       y=x/25+1
       print("---------------数据写入成功（%d/10）------------" %y)
       time.sleep(1)
