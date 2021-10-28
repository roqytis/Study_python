#Beautiful 메소드 연습
from bs4 import BeautifulSoup

html_page = """
<html>
<body>
<h1>제목 태그</h1>
<p>웹문서 일기</p>
<p>원하는 자료 선택</p>
</body>
</html>
"""

print(type(html_page)) #<class 'str'>
soup = BeautifulSoup(html_page,'html.parser') #BeautifulSoup 객체 생성
print(type(soup)) #<class 'bs4.BeautifulSoup'>
print()
h1 = soup.html.body.h1
print('h1 : ',h1.string)
print('h1 : ',h1.text)
print()
p1= soup.html.body.p
print('p1 : ', p1.text)
p2 = p1.next_sibling.next_sibling#DOM(document object model)을 이용한 처리에는 한계가 있다. 해결법 : BeautifulSoup
print('p2: ', p2.text)

print('-----------------find-------------------------')
html_page2 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>웹문서 일기</p>
<p id="my" class="our">원하는 자료 선택</p>
</body>
</html>
"""

soup2 = BeautifulSoup(html_page2,'html.parser')
print(soup2.p,' ',soup2.p.string)
print(soup2.find('p').string) #최초의 tag를 찾음
print(soup2.find('p', id='my').string)
print(soup2.find_all('p')) #해당 tag 모두 찾음
print(soup2.find(id='my').string)
print(soup2.find(class_='our').string)
print(soup2.find(attrs ={'class':'our'}).string)

print('-------------------------------')
html_page3 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>웹문서 일기</p>
<p id="my" class="our">원하는 자료 선택</p>
<div>
   <a href="https://www.naver.com">네이버</a><br>
   <a href="https://www.daum.net">다음</a>
</div>
</body>
</html>
"""

soup3 = BeautifulSoup(html_page3,'lxml')
print(soup3.find_all('a'))
print(soup3.findAll('a'))
print(soup3.find_all(['a','p']))

print(soup3.find_all(['p'],'our')) #p 태그 중에서 class가 'our'
print(soup3.find_all(['p'],{'id':'my'})) #p 태그 중에서 id가 'my'

print()
links = soup3.find_all('a')
for i in links:
    href = i.attrs['href']
    text = i.string
    print(href,' ',text)
    
    
print('정규 표현식---')
import re 
links2 = soup3.find_all(href=re.compile(r'^http'))
print(links2)
for k in links2:
    print(k.attrs['href'])
    
print()    



print('select 함수 : css의 selector를 사용 ---')
html_page4 = """
<html>
<body>
<div id="hello">
   <a href="https://www.naver.com">네이버</a><br>
   <a href="https://www.korea.com">코리아</a><br>
   <span>
      <a href="https://www.daum.net">다음</a>
   </span>
   <ul class="world">
        <li>안녕</li>
        <li>반가워</li>
   </ul>
</div>
<div id="hi" class="good">second div</div>
</body>
</html>
"""
soup4 = BeautifulSoup(html_page4,'lxml')
print(soup4.select_one("div#hi")) #단수 선택
print(soup4.select_one("div.good")) #단수 선택 클래스중에서 첫번쨰 꺼
print(soup4.select_one("div > a")) #단수 선택 클래스중에서 첫번쨰 꺼

print()
print(soup4.select("div > a")) #복수 선택 div의 자식 a
print(soup4.select("div > a")) #복수 선택 div의 자손 a

aa = soup4.select("div#hello ul.world > li") 
print(aa)
for i in aa:
    print('li : ',i.string)

print()
#DataFrame에 담기
msg = list()
for i in aa:
    msg.append(i.string)
    
print(msg, type(msg))

import pandas as pd
df = pd.DataFrame(msg, columns=['aa'])
print(df)
print(type(df))


#////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
#"https://music.bugs.co.kr이 지운하는 음악 순위
from urllib.request import urlopen
url = urlopen("https://music.bugs.co.kr/chart?wl_ref=M_left_02_01")
soup = BeautifulSoup(url.read(), 'html.parser')
# td 태그에 check라는 class가 있는 td 태그를 모두 가져온다.
musics = soup.find_all('td', "check")
 
for i, music in enumerate(musics):   # musics의 각 태그들에 대해서
    # input 태그안에 title 속성값을 parsing한다. 
    print("{}위: {}".format(i+1, music.input['title']))
    # print("{}위: {}".format(i + 1, music.find('input')['title']))
'''