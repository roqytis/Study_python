#그룹화 : group by, pivot, pivot_table

import numpy as np
import pandas as pd

data = {'city':['강남','강북','강남','강북'],
        'year':[2000,2001,2002,2002],
        'pop' : [3.3,2.5,3.0,2.0]}
print(data)

df = pd.DataFrame(data)
print(df)

print()
print(df.groupby(['city']).sum())
print(df.groupby(['city','year']).mean())

print()
print(df.pivot('city', 'year', 'pop'))

print()
print(df)
print()
print(df.pivot_table(index= ['city'])) #aggfunc = np.mean 기본값
print(df.pivot_table(index= ['city'], aggfunc = np.mean)) #aggfunc = np.mean 기본값
print(df.pivot_table(index= ['city','year'], aggfunc = np.mean)) #aggfunc = np.mean 기본값
print(df.pivot_table(index= ['city','year'], aggfunc = [len, np.sum])) #aggfunc = np.mean 기본값

print()
print(df.pivot_table(values=['pop'],index=['city']))
print(df.pivot_table(values=['pop'],index='city', aggfunc = len))

print()
print(df.pivot_table(values = ['pop'], index = ['year'], columns = ['city']))
print(df.pivot_table(values = ['pop'], index = ['year'], columns = ['city'], margins= True))
print(df.pivot_table(values = ['pop'], index = ['year'], columns = ['city'], margins= True, fill_value = 0))