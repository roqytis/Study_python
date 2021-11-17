import pandas as pd
import numpy as np
import scipy.stats as stats

# [one-sample t 검정 : 문제1]  
# 영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다.
# 한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간을 수집하여 다음의 자료를 얻었다. 
# 한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
# 305 280 296 313 287 240 259 266 318 280 325 295 315 278

data = pd.DataFrame([305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278], columns=['수명'])
#print(data)
print('새로운 백열전구 평균 : ', np.mean(data))   # 두 개의 평균 289.785714, 300 사이에 유의한 차이가 있는가?
#귀무 : 한국연구소에서 개발한 백열전구의 수명은 300시간이다.
#대립 : 한국연구소에서 개발한 백열전구의 수명은 300시간이 아니다.

result = stats.ttest_1samp(data, popmean = 300)
print(result) #pvalue=0.14360625 > 0.05이므로 귀무가설을 채택.
# 한국연구소에서 개발한 신형 백열전구의 수명은 평균 300시간이다.

print('----------------------')
# [one-sample t 검정 : 문제2] 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. 
# A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")

#귀무 : A회사의 노트북 평균 사용시간이 5.2시간이다
#대립 : A회사의 노트북 평균 사용시간이 5.2시간이 아니다
data = pd.read_csv('../testdata/one_sample.csv')
print(data.head(10))
data.time = data.time.replace("     ", "")
data['time'] = pd.to_numeric(data['time'])
print(data['time'].mean())   # 5.5568, 5.2 평균에 차이가 있는가?
print(data['time'].isnull().sum())  # 41
data = data.dropna(axis = 0, how = 'any')
result = stats.ttest_1samp(data['time'], popmean = 5.2)
print(result)   # pvalue=0.00014166 < 0.05이므로 귀무기각, 대립가설 채택
# A회사의 노트북 평균 사용시간이 5.2시간이 아니다.


print('----------------------')
#[one-sample t 검정 : 문제3] 
#http://www.price.go.kr에서 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료를 파일로 받아 미용요금을 얻도록 하자. 
#정부에서는 전국평균 미용요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.

# 귀무 : 전국 평균 미용요금은 15000원 이다.
# 대립 : 전국 평균 미용요금은 15000원이 아니다.
import numpy as np
import scipy.stats as stats
import pandas as pd

#data = pd.read_excel("개인서비스지역별_동향2021-09월112-11시36분.xls", sheet_name="sheet1", encoding='UTF-8')
data = pd.read_csv("개인서비스지역별_동향2021-09월112-11시36분.csv")
print(data)
print(np.mean(data.가격)) # 실제 전국 평균 미용가격은 16308.1875원 / 과연 정부발표 평균과 실제평균사이에는 통계적으로 유의미한 차이가 있나?
print('정규성 확인 :',stats.shapiro(data.가격)) # pvalue=0.371421217918396 > 0.05 이므로 정규성 만족
result = stats.ttest_1samp(data['가격'], popmean = 15000) # 귀무가설에서의 평균값은 15000
print(result) # pvalue=0.00854196 < 0.05 이므로 귀무가설 기각. 대립가설 채택.
# 따라서 전국 평균 미용요금은 15000원이 아니다.
