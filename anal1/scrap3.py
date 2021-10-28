#웹 스크래핑 연습1
import requests
import urllib.request as req
from bs4 import BeautifulSoup

# 연습1 : 위키백과에서 이순신 검색 결과 읽기
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
print(wiki) #<http.client.HTTPResponse object at 0x00000187F8E3B6D0>

#파싱하기
soup = BeautifulSoup(wiki, 'html.parser')
#print(soup)
#print(soup.select("#mw-content-text > div.mw-parser-output > p"))

ss= soup.select("div.mw-parser-output > p")
for s in ss:
    if(s.string!=None):
        print(s.string)
        
print('---------------')
#연습2 :daum 사이트이 뉴스 중 사회면 a tag 읽기
url = "https://news.daum.net/society#1"
daum = req.urlopen(url)
print(daum)

soup = BeautifulSoup(daum,'lxml')
print(soup.select_one("#kakaoGnb > div > ul > li.on > a > span").string)

# 메뉴 : 홈 사회 정치 경제 문화... tv

#여러 개의 a tag의 string 중 3개만 출력
url = "https://news.daum.net/"
daum = req.urlopen(url)
print(daum)

soup = BeautifulSoup(daum,'lxml')
print(soup.select("#kakaoGnb > div" ))
