# pandas : stack, unstack, 범주화, merge
import pandas as pd
import numpy as np

df = pd.DataFrame(1000 + np.arange(6).reshape(2,3), index = ['대전','서울'],
                  columns = ['2020', '2021','2022'])

print(df)
print(df.T)

print()
df_row = df.stack() #index를 기준으로 칼럼 쌓기
print(df_row)

df_col = df_row.unstack() # stack 원복
print(df_col)

#범주화(구간 나누기) cut()
price = [10.3,5.5,7.8,3.6]
cut = [3,7,9,11] #구간 기준 값
result_cut = pd.cut(price, cut)
print(result_cut) #[(9, 11], (3, 7], (7, 9], (3, 7]]  #(a,b] <== a < x <=b
print(pd.value_counts(result_cut))



print() #qcut()
datas = pd.Series(np.arange(1,1001))
print(datas.tail(3))

#cut2 = [1,500,1000]
#result_cut2 = pd.cut(datas, cut2)
#print(result_cut2)

result_cut2 = pd.qcut(datas, 3) # 지정한 숫자 만큼 범주화
print(result_cut2)
print(pd.value_counts(result_cut2))

print()
group_col = datas.groupby(result_cut2)
print(group_col)
print(group_col.agg(['count','mean','std','min'])) #그룹 데이터에 대해 함수를 실행

#agg 대신 함수 작성
def my_func(gr):
    return {'count':gr.count(), 'mean':gr.mean(), 'std':gr.std(), 'min':gr.min()}
print(group_col.apply(my_func))
print()
print(group_col.apply(my_func).unstack())

print('-------------')
df1 = pd.DataFrame({'data1': range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
print(df2)
print()
print(pd.merge(df1, df2, on = 'key')) #key를 기준으로 병합 (inner join :교집합)
print()
print(pd.merge(df1, df2, on = 'key',how='inner'))

print()
print(pd.merge(df1, df2, on = 'key',how='outer'))
print()
print(pd.merge(df1, df2, on = 'key',how='right'))
print()
print(pd.merge(df1, df2, on = 'key',how='left'))

print()
df3 = pd.DataFrame({'key2':['a','b','d'], 'dtat2':range(3)})
print(df3)
#df1과 df3합치기
print(pd.merge(df1,df3,left_on='key',right_on='key2'))
print()
print(pd.concat([df1,df3],axis = 0))
print(pd.concat([df1,df3],axis = 1))