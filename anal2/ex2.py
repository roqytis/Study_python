# 위키백과에서 이순신 검색 결과를 읽어 형태소 분석 후 단어 수 출력
import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse # 한글 인코딩용

okt = Okt()

para = parse.quote('이순신')
url = "https://ko.wikipedia.org/wiki/" + para
#print(url)

page = urllib.request.urlopen(url).read().decode()
#print(page)
soup = BeautifulSoup(page,'html.parser')
#print(soup)

wordlist =[]

for item in soup.select("#mw-content-text > div > p"):
    #print(item)
    if item.string != None:
        ss = item.string
        wordlist += okt.nouns(ss)
        
print('wordlist : ',wordlist)
print('단어 수 : ' + str(len(wordlist)))
print('중복을 제거한 단어 수: ', len(set(wordlist)))

# 단어별 발생횟수를 dict type으로 기억
word_dict = {}
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
        
print('word_dict: ',word_dict)

print('pandat의 Series로 출력 ---')
import pandas as pd

woList = pd.Series(wordlist)
print(woList[:3])
print(woList.value_counts()[:5])

print()
woDict = pd.Series(word_dict)
print(woDict[:3])
print(woDict.value_counts())

print('pandat의 DataFrame로 출력 ---')
df1 = pd.DataFrame(wordlist,columns=['단어'])
print(df1.head(5))

print()
df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
print(df2)
df2=df2.T
df2.columns = ['단어','빈도수']
print(df2.head(5))
#print(df2.values)

df2.to_csv('이순신.csv', sep = ',', index = False)
df3 = pd.read_csv('이순신.csv')
print()
print(df3.head(5))