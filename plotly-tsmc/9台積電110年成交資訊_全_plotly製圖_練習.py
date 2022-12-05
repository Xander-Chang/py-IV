#!!! 舊 csv 檔案要刪掉才可以執行 不然 'append file' 會接著要寫下去，程式錯誤
# plotly 繪圖練習

import json, requests, csv, os, time
import pandas as pd
import matplotlib.pyplot as plt

# plotly
from plotly.offline import plot
import plotly.graph_objs as go


# 1. 轉換日期 為'西元年'
def chronology(date):
    original_str = str(date)
    original_year = original_str[0:3]
    changed_year = str(int(original_year) + 1911)
    changed_date = changed_year + original_str[4:6] + original_str[7:9]
    return changed_date


# 2. 設定月份網址格式
def add_month(n):
    if (n < 10):
        month = '0' + str(n)
    else:
        month = str(n)
    return month



urlbase = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021'  #網址前半
urltail = '01&stockNo=2330'  # 網址後半共同的部分



# 3. 建立、寫入檔案 csv
if not os.path.isfile('9台積電110年交易資訊.csv'):
    for i in range(1, 13):  # 取1到12數字
        # 組合網址、 json 解析
        url_all = urlbase + add_month(i) + urltail
        print(i,'月的網址:',url_all)
        html_all = requests.get(url_all)
        pyjson_all = json.loads(html_all.text)

        # 4. 建檔 寫入
        with open('9台積電110年交易資訊.csv','a', encoding='utf-8-sig', newline='') as f:
            csv_Writer = csv.writer(f)
            if i == 1:
                csv_Writer.writerow(pyjson_all['fields'])
            for row in pyjson_all['data']:
                csv_Writer.writerow(row)

        
        print('休息10秒')
        time.sleep(10)


# 5. 整理資料
pd_csv = pd.read_csv('9台積電110年交易資訊.csv', encoding='utf-8-sig')
for i in range(len(pd_csv['日期'])):
    pd_csv['日期'][i] = chronology(pd_csv['日期'][i])   # 改變數字
    print(pd_csv['日期'][i])
# 改變 資料型態 為日期
pd_csv['日期'] = pd.to_datetime(pd_csv['日期'])


# 6. 製圖
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
'''
pd_csv.plot(kind='line', x='日期', y=['收盤價', '最低價', '最高價'], figsize=[12,8])
plt.show()
'''


# plotly 繪圖
'''
trace1 = go.Scatter(x=pd_csv['日期'], y=pd_csv['收盤價'], name='收盤價')
trace2 = go.Scatter(x=pd_csv['日期'], y=pd_csv['最低價'], name='最低價')
trace3 = go.Scatter(x=pd_csv['日期'], y=pd_csv['最高價'], name='最高價')
'''
data = [go.Scatter(x=pd_csv['日期'], y=pd_csv['收盤價'], name='收盤價'),
        go.Scatter(x=pd_csv['日期'], y=pd_csv['最低價'], name='最低價'),
        go.Scatter(x=pd_csv['日期'], y=pd_csv['最高價'], name='最高價')]

# 數字代表 幾個函數 方法

title3 = dict(text='台積電110年交易資訊 統計圖', x=0.5, font=dict(family='STKaiti',size=30,color='rgba(239, 12, 111, 0.7)'))
xaxis3 = dict(title='日期', tickangle= -30, titlefont=dict(size=20,color='rgb(202,0,156)'))
yaxis3 = dict(title='價格', tickangle= 30, titlefont=dict(size=20, color='rgb(60,180,200)'))

Layout = go.Layout(template='seaborn', title=title3, xaxis=xaxis3, yaxis=yaxis3)


Figure = go.Figure(data, Layout)

plot(Figure, filename='台積電110年交易資訊圖.html', auto_open=False)