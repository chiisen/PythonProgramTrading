from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
#options.add_argument('headless')

service = Service(executable_path='.\chromedriver-win64\chromedriver.exe')
web = webdriver.Chrome(service=service, options=options)

web.get('https://www.twse.com.tw/zh/')
print(web.page_source)
web.quit()