import requests
from bs4 import BeautifulSoup

# 修正 403 問題
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
req = requests.get('https://fubon-ebrokerdj.fbs.com.tw/z/zg/zg_A_0_5.djhtm', headers=headers)
# 取得網頁原始碼文字
html = req.text
# 將網頁原始碼轉為 Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# 取出所有商品欄位
product = [i.text.strip() for i in soup.find_all('td', class_='t3t1')]
# 顯示
print(product)
