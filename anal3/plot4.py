# 웹에서 특정단어 검색 후 해당 문서를 스크래핑한다. 명사들만 골라 빈도 수 구한 다음 워드클라우드 그리기
from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import quote

keyword = input('검색어 : ') # 키보드로 검색할 단어 입력받기
#print(keyword)
#print(quote(keyword)) # quote 입력받은 키워드(한글)를 인코딩함

target_url ="https://www.donga.com/news/search?query=" +quote(keyword)
print(target_url)
source_data = req.urlopen(target_url)
soup = BeautifulSoup(source_data, 'html.parser', from_encoding='UTF-8')
#print(soup)
msg =""
for title in soup.find_all('p','tit'):
    title_link = title.select('a')
    #print(title_link)
    article_url = title_link[0]['href'] # 검색어에서 href 태그 즉, url링크만 따오기
    # print(title_link) 출력해보시면 리스트로 나오는데 그중에 href 태그만 가져오는거
    #print(article_url)
    try:
        source_article = req.urlopen(article_url)
        soup = BeautifulSoup(source_article, 'html.parser', from_encoding='utf-8')
        #print(soup)
        contents = soup.select('div.article_txt')
        #print(contents)
        for imsi in contents:
            item = str(imsi.find_all(text=True)) # text 데이터가 있는것만 읽어옴
            #print(item)
            msg = msg+item
        
    except Exception as e:
        pass

#print(msg)

from konlpy.tag import Okt
from collections import Counter # (단어) 개수를 세주는 라이브러리
okt = Okt()
nouns = okt.nouns(msg) # msg 에서 명사만 읽어옴
#print(nouns)
result =[]
for imsi in nouns:
    if len(imsi) >1: # 명사 중 두글자 이상만 저장됨
        result.append(imsi)
        
print(result)
count = Counter(result)
print(count) # 많이 출현한 단어순으로 출력
tag = count.most_common(50) # 많이 출현한 단어순으로 상위 50개만 tag에 저장

# 워드 클라우드 작성
#pip install pygame
#pip install simplejson
#pip install pytagcloud 3가지 설치 필요

import pytagcloud
taglist = pytagcloud.make_tags(tag, maxsize=100) # 태그의 최대 크기를 100으로 제한
print(taglist)

pytagcloud.create_tag_image(taglist, "word.png", size=(1000,600), fontname="Korean", rectangular=False)
# word.png 태그리스트를 이미지로 저장 / 크기, 폰트 설정 / 사각형옵션은 끔

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("word.png")
plt.imshow(img)
plt.show()

import webbrowser
webbrowser.open("word.png")