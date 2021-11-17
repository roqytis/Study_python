# 이원카이제곱 검정
#두 개 이상의 집단 또는 범주의 변인을 대상으로 독립성, 동질성 검정
#교차표를 사용
#독립성(관련성) 검정
# - 동일 집단의 두 변인 (학력수준과 대학진학 여부)을 대상으로 관련성이 있는가 없는가?
#ㄷ- 독깁성 검정은 두 변수 사이의 연관성을 검정한다.

#교육수준(독립 - 집단) 과 흡연율 (종속 - 빈도 ㅅ, 비율) 간의 관련성 분석 : smoke.csv
#귀무 : 교육 수준과 흡연율 간에는 관련이 없다. (독립니다)
#대립 : 교육수준과 흡연율 간에는 관련이 있따. (독립이 아니다)

import pandas as pd
import scipy.stats as stats

data = pd.read_csv('../testdata/smoke.csv')
print(data.info())
print(data.head(3))
print(data.education.unique())
print(data['smoking'].unique())

ctab = pd.crosstab(index = data['education'],columns = data['smoking']) # , normalize=True :비율로 출력, 구성 비율로 교차표 생성
ctab.index = ['대학원졸','대졸','고졸']
ctab.columns = ['과흡연','보통','노담']
print(ctab)

chi_result = [ctab.loc['대학원졸'],ctab.loc['대졸'],ctab.loc['고졸']]
#chi2, p, ddof, expected = stats.chi2_contingency(chi_result)
chi2, p, ddof, expected = stats.chi2_contingency(ctab)
print('chi2: ',chi2) #18.910915739853955
print('p: ',p) #0.0008182572832162924
print('ddof : ',ddof) # 4 : (3-1)*(3-1)
print('expected: ',expected) #  [[68.94647887 83.8056338  58.24788732]
# [16.9915493  20.65352113 14.35492958]
 #[30.06197183 36.54084507 25.3971831 ]]

#해석: p-value 0.000818 < 0.05 유의미한 수준에서 귀무가설을 기각
#대립가설인 교육수준과 흡연율 간에는 관련이 있다를 채택.

#참고 : 분할표의 자유도가 1인 경우는 x^2값이 약간 높게 계산된다. 그래서 아래의 식과 같이 절대값 |o-E|에서 0.5를 뺀 다음 제곱하며,
#이 방법을 야트보정이라 한다. 파이썬은 자동 처리됨.
# x^2=시그마(|O-E|-o.5)^2/E

print('----------------------------')
# 실습) 국가전체와 지영게 대한 인종 간 인원수로 독립성 검정 실습
# 두 집단(국간전체-national, 특저지역 - la)의 인종 간 인원수의 분포가 관련이 있는가?
national= pd.DataFrame(["white"]*100000 + ["hispanic"]*600000+
                       ["black"]* 600 + ["asian"]*15000 +["other"]* 35000)
la = pd.DataFrame(["white"]*600 + ["hispanic"]*300+
                       ["black"]* 250 + ["asian"]*75 +["other"]* 150)
#귀무가설 : 국가전체와 지역에 대한 인종 간 인원수는 관련이 없다. #인원수의 분포가 독립
#대립가설 : 국가전체와 지역에 대한 인종 간 인워수는 관련이 있다.
#print(national)
na_table = pd.crosstab(index = national[0],columns='count')
la_table = pd.crosstab(index = la[0], columns= 'count')
print(na_table)
print()
na_table['count_la']= la_table['count']
print(na_table)
chi2,p,df,_ = stats.chi2_contingency(na_table)
print('chi2,p,df: ', chi2,p,df)
#해석: p-value: <0.05 귀무가설을 기각하고 대립가설