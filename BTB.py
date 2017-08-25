import requests
from bs4 import BeautifulSoup
import re
import json
import pandas
import matplotlib
import pylab
res=requests.get('https://www.coingecko.com/zh/%E4%BB%B7%E6%A0%BC%E8%B5%B0%E5%8A%BF%E5%9B%BE/%E6%AF%94%E7%89%B9%E5%B8%81/usd',headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
soup=BeautifulSoup(res.text,'html.parser')
data_prices=soup.select('#coin_maxd_historical_price_chart')[0].prettify('utf-8').decode('utf-8')
n=re.search('<div data-prices="(.*?)"',data_prices)
jd=json.loads(n.group(1))
df=pandas.DataFrame(jd)
df.columns=['datetime','twd']
df['datetime']=pandas.to_datetime(df['datetime'],unit='ms')
df.index=df['datetime']

df['ma7']=df['twd'].rolling(window=7).mean()#7天平均值

df2=df[df['datetime']>='2017-01-01']
pylab.figure(figsize=(14,6))#设置大小

pylab.plot(df2[['twd','ma7']])
pylab.xlabel(u'datetime')
pylab.ylabel(u'price(usd)')
pylab.title('Bitcoin price chart')
pylab.show()