from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid=NkQ2M0YzQUYwMDQyNzhBNDRFNzhGNDBENTRBMkZDNUY=')
html_text=browser.page_source
print(html_text)()