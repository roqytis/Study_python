#웹 스크래핑 후 읽은 자료를 뷰티플스프로 파싱을 한 후 원하는 자료를 추출
#뷰티플스프 대상문서는 XML, HTML, Json은 안됨

#웹문서 읽기
import requests
from bs4 import BeautifulSoup

def scrap_func():
    base_url = "http://www.naver.com/index.html"
    source_code = requests.get(base_url).text
    #print(source_code) #class 'str'
    
    convert_data = BeautifulSoup(source_code, 'html.parser') #parsing
    print(type(convert_data)) #<class 'bs4.BeautifulSoup'> beautifulsoup의 find,select 메서드 사용가능
    
    aa = convert_data.findAll('a')
    print(aa)
    
    for atag in convert_data.findAll('a'):
        href = atag.get('href')
        title = atag.string
        print(href)    
        print(title)
        
if __name__ == '__main__':
    scrap_func()