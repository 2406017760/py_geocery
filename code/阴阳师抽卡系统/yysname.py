from selenium import webdriver
from time import sleep
import lxml
import random
from lxml import etree
browser = webdriver.Chrome()
browser.get('http://yys.163.com/index.html')
sleep(1)
element=browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]")
element.click()
sleep(1)
element=browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/a[3]")
element.click()
html_text=browser.page_source
html1=etree.HTML(html_text)
sp_name=html1.xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/ul/li[*]/p/text()")
print(sp_name)
element=browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/a[4]")
element.click()
html_text=browser.page_source
html1=etree.HTML(html_text)
ssr_name=html1.xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/ul[1]/li[*]/p/text()")
print(ssr_name)
element=browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/a[5]")
element.click()
html_text=browser.page_source
html1=etree.HTML(html_text)
sr_name=html1.xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/ul[1]/li[*]/p/text()")
print(sr_name)
element=browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/a[6]")
element.click()
html_text=browser.page_source
html1=etree.HTML(html_text)
r_name=html1.xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/ul[1]/li[*]/p/text()")
print(r_name)
