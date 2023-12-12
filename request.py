import requests

html = requests.get('https://tw.stock.yahoo.com/rank/change-up?exchange=TAI')  # 取得網頁內容

print(html.text)  # 查看網頁內容
