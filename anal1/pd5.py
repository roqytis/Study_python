# pandas로 파일 입출력
import pandas as pd

#df = pd.read_csv('../testdata/ex1.csv')
df=pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex1.csv')

print(df, type(df))
print(df.info())

print('--------------------------------------')
#df = pd.read_table('../testdata/ex1.csv', sep=',')
df = pd.read_table('../testdata/ex1.csv', sep=',',skipinitialspace=True) #칼러명 앞에 공백 제거
print(df)

print()
#df = pd.read_csv('../testdata/ex2.csv', header=None)
df = pd.read_csv('../testdata/ex2.csv', header=None, names=['a','b','c','d','e'])
print(df)

print()
#df = pd.read_csv('../testdata/ex3.txt')
df = pd.read_csv('../testdata/ex3.txt', sep='\s+')
print(df)
print(df.info())

print()
df = pd.read_fwf('../testdata/data_fwt.txt',widths = (10,3,5),
                  header = None, names=('date','name','price'),encoding='UTF-8')
print(df)

#chunk: 용량이 큰 파일을  원하는 크기 만큼 분리해서 읽기
test = pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize = 3)
print(test) #<pandas.io.parsers.TextFileReader object at 0x0000011A8E1E49D0>

for p in test:
    #print(p)
    print(p.sort_values(by=2,ascending=True))
print('--------------------------')
items = {'apple':{'count':10, 'price':1500},'orange':{'count':3, 'price':500}}
df = pd.DataFrame(items)
print(df)

df.to_clipboard()   #클립 보드 이용하면 개꿀 
print(df.to_html())  #이거 꼭 알아둬야함
print(df.to_csv())
print(df.to_json())
print(df.to_dict())
#...

df.to_csv('result1.csv', sep = ',') #액샐 만들어 버리기
df.to_csv('result2.csv', sep = ',', index = False) #액샐 만들어 버리기
df.to_csv('result3.csv', sep = ',', index = False, header= False) #액샐 만들어 버리기

data = df.T
print(data)
df.to_csv('result4.csv', sep = ',', index = False, header= True)

redata = pd.read_csv('result4.csv')
print(redata)

print('-------엑셀-----------')
df2 = pd.DataFrame({'data':[10,20,30,40,50]})
print(df2)
wr = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
df2.to_excel(wr,sheet_name='Sheet1')
wr.save()

sou = pd.ExcelFile('result.xlsx')
print(sou.sheet_names) #['Sheet1']
exdf = sou.parse('Sheet1')
print(exdf)

print()
exdf2 = pd.read_excel(open('result.xlsx','rb'), sheet_name = 'Sheet1')
print(exdf2)

print('----------------------------------------')

df5 = pd.read_csv('../testdata/titanic_data.csv')
print(df5)