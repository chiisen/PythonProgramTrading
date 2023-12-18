# pandas 不要和 py 檔同名，會報錯要你 import pandas 套件，例如: py 檔名為 pandas.py
import pandas as pd
import numpy as np

# 建立氣溫和降雨量的 DataFrame
temperature_data = {'日期': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04'],
                    '氣溫': [23.1, 25.4, 27.6, 26.9]}

temperature_df = pd.DataFrame(temperature_data)

rainfall_data = {'日期': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04'],
                 '降雨量': [0.0, 0.2, 0.1, 0.4]}

rainfall_df = pd.DataFrame(rainfall_data)

# 將日期欄位轉換為 DataFrame 格式，方便後續處理
temperature_df['日期'] = pd.to_datetime(temperature_df['日期'])
rainfall_df['日期'] = pd.to_datetime(rainfall_df['日期'])

# 將兩個 DataFrame 合併，使用日期欄位作為鍵值
merged_df = pd.merge(temperature_df, rainfall_df, on='日期')

print(merged_df)


# 將日期欄位轉換為 DataFrame 格式，方便後續處理
temperature_df.index = pd.to_datetime(temperature_df['日期'])
rainfall_df.index = pd.to_datetime(rainfall_df['日期'])

# 使用 pd.concat() 將兩個 DataFrame 沿著列的方向合併
concat_df = pd.concat([temperature_df, rainfall_df], axis=1)

print(concat_df)
