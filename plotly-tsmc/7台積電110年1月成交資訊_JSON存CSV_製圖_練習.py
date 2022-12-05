# 繪製[收盤價，最高價，最低價]
# 改成西元年

import json, requests, csv, os
import pandas as pd
import matplotlib.pyplot as plt

# 連接網址
url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210101&stockNo=2330'
html = requests.get(url)

# 轉換資料型態為 python
py_json = json.loads(html.text)

# 寫入 存成CSV檔案
with open('7台積電110年1月成交資訊.csv','w',encoding='utf-8-sig', newline='') as f:
    csv_Writer = csv.writer(f)
    # 寫入標頭
    csv_Writer.writerow(py_json['fields'])
    # 寫入一行一行的資料
    for row in py_json['data']:
        csv_Writer.writerow(row)


# 轉換日期 為'西元年'
def chronology(date):
    original_str = str(date)
    original_year = original_str[0:3]
    changed_year = str(int(original_year) + 1911)
    changed_date = changed_year + original_str[4:6] + original_str[7:9]
    return changed_date




# 讀 CSV 、 整理資料
# 方法一: 用 pandas

pd_csv = pd.read_csv('7台積電110年1月成交資訊.csv', encoding='utf-8')
#print(pd_csv)
#print(pd_csv['日期'])
for i in range(len(pd_csv['日期'])):
    pd_csv['日期'][i] = chronology(pd_csv['日期'][i])

# 轉成日期型態!!!!!
pd_csv['日期'] = pd.to_datetime(pd_csv['日期'])
# 繪圖
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

pd_csv.plot(kind='line', x='日期', y=['收盤價','最高價','最低價'], figsize=[12,8])
plt.show()




# 方法二:
'''
new_date = []
end_price, highest, lowest = [], [], []
with open('7台積電110年1月成交資訊.csv',encoding='utf-8') as f:
    csv_Reader = csv.DictReader(f)
    List_csv = list(csv_Reader)
    #print(List_csv)
    for data in List_csv:
        new_date.append(chronology(data['\ufeff日期']))
        end_price.append(chronology(data['開盤價']))
        highest.append(chronology(data['最高價']))
        lowest.append(chronology(data['最低價']))
print(new_date)
print(end_price)
print(highest)
print(lowest)
'''









