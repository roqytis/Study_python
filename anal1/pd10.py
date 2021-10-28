# 웹문서 중 json data 처리
import urllib.request as req
import json

url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5/"
plainText = req.urlopen(url).read().decode()
# print(plainText, type(plainText) # <class 'str'>

jsonData = json.loads(plainText)  # json decoding str -> dict
# print(jsonData, type(jsonData)) # class 'dic'

# dict type의 get 함수 사용
libData = jsonData.get('SeoulLibraryTime').get('row')
print(libData)

name = libData[0].get('LBRRY_NAME')
print(name)

print()
datas = []
for a in libData:
    name = a.get('LBRRY_NAME')
    tel = a.get('TEL_NO')
    addr = a.get('ADRES')
    print(name + '\t' + tel + '\t' + addr)
    imsi = [name, tel, addr]
    datas.append(imsi)

import pandas as pd
df = pd.DataFrame(datas, columns=['이름', '전화번호', '주소'])
print(df)