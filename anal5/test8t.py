# 어느 음식점의 매출 데이터와 날씨 데이터를 활용하여 강수 여부에 따른 매출의 평균에 차이가 있는지 검정

# 원본소스는 data.go.kr
# 귀무 가설 : 매출액은 강수의 영향과 관련이 없다.
# 대립 가설 : 매출액은 강수의 영향과 관련이 있다.


import numpy as np
import scipy.stats as stats
import pandas as pd

# 매출 데이터 읽기

sales_data = pd.read_csv("../testdata/tsales.csv", \
                         dtype = {'YMD':'object'})
print(sales_data.head(3))
print(sales_data.info())

wt_data = pd.read_csv("../testdata/tweather.csv")
print(wt_data.head(3))
print(wt_data.info())


print()

# sales_data 날짜를 기준으로 join 하기위해 wt_data의 tm 칼럼을 변경 (2018-06-01 -> 20180601)

wt_data.tm = wt_data.tm.map(lambda x: x.replace('-',''))
print(wt_data.head(3))

print()
frame = sales_data.merge(wt_data, how = 'left', left_on='YMD', right_on = 'tm')
print(frame.head(5)) # 328 rows x 12 columns
print(frame.columns) # Index(['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn','maxWs', 'avgWs', 'ddMes'],

data = frame.iloc[:, [0,1,7,8]]

print(data.head(3))
print(data.isnull().sum())

print('/n--독립표본 t 검정-------')
#print(data['sumRn'] > 0)
#data['rain_yn'] = (data['sumRn'] > 0).astype(int)
#print(data.head(3))


#print((True*1,' ', False*1))
data['rain_yn'] = (data.loc[:,('sumRn')] > 0)*1
print(data.head(3))

#강수여부와 매출액 시각화
import matplotlib.pyplot as plt

sp = np.array(data.iloc[:,[1,4]])
#print(sp)
tg1 = sp[sp[:,1] == 0, 0] # 비 안올때 매출액
tg2 = sp[sp[:,1] == 1, 0] # 비 올때 매출액

#plt.plot(tg1)
#plt.show()

#plt.plot(tg2)
#plt.show()

plt.boxplot([tg1,tg2], meanline=True, showmeans=True, notch=True)
plt.show()

# 두 집단 평균
print(np.mean(tg1),' ', np.mean(tg2)) #761040.25   757331.52
print(761040.25 - 757331.52) #3708.72 매출액 평균에 차이가 있다고 할 수 있는가?

#정규성 검정
print(len(tg1),' ',len(tg2))
print(stats.shapiro(tg1).pvalue) #0.0560 >0.05 만족
print(stats.shapiro(tg2).pvalue) #0.8827 > 0.05 만족

#등분산성
print(stats.levene(tg1,tg2).pvalue) # 0.7123 > 0.05 만족

result = stats.ttest_ind(tg1, tg2, equal_var = True)
print(result)
print('t value : ', result[0])  #t value :  0.10109828602924716
print('p value : ', result[1]) #p value :  0.919534587722196
#매출액은 강수의 영향과 관련이 없다. 