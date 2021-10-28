#xml 웹문서 일기: 기상청 제공 날씨 정보
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url= "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = urllib.request.urlopen(url).read()
#print(data.decode('utf8'))

soup = BeautifulSoup(data,'lxml')
#print(soup)
title = soup.find('title').string
#print(title)

wf= soup.find('wf')
print(wf)

city = soup.find_all('city')
#print(city)
cityData= []
for c in city:
    cityData.append(c.string)
df= pd.DataFrame()
df['city']= cityData
print(df.head(2))

tempMins = soup.select('location > province + city + data > tmn')
tempData = []
for t in tempMins:
    tempData.append(t.string)

df['temp_min']= tempData
df.columns = ['지역', '최저기온']
print(df.head(5))

#df.to_csv('날씨정보.csv', index= False)

print(df[0:5])
print()
print(df.tail(3))
print(df[-3:len(df)])

print()
df= df.astype({'최저기온':int})
print(df.info())
print(df['최저기온'].mean(),df['최저기온'].std())

print()
print(df.loc[df['최저기온'] >= 12])