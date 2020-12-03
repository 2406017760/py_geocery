import requests
from selenium import webdriver
from fake_useragent import UserAgent
ua = UserAgent()
url="http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid=NkQ2M0YzQUYwMDQyNzhBNDRFNzhGNDBENTRBMkZDNUY='"
headers = {
    'User-Agent':ua.random
    } 
