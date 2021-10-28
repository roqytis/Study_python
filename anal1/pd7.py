#웹 스크래핑 : 일정 간격으로 읽기
from bs4 import BeautifulSoup
import urllib.request as req
import time
import datetime

def working():
    url= "https://finance.naver.com/marketindex"
    data= req.urlopen(url)
    
    soup = BeautifulSoup(data,'html.parser')
    price = soup.select_one("div > span.value").string
    print('미국 usd: ', price)
    
    t= datetime.datetime.now()
    #print(t) #2021 - 10 - 27
    fname= './usd/'+ t.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    #print(frame)
    
    with open(fname,'w') as f:
        f.write(price)
    
while True:
    working()
    time.sleep(5)