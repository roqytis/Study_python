#이원카이제곱

 #동질성 검정 - 두 집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다. 두집단 이상에서 각 범주(집단) 간의 비율이 서로
 #동일한가를 검정하게 된다. 두 개 이상의 범주형 자료가 동이한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다.
 #동질성 검정실습1) 교육방법에 따른 교육생들의 만족도 분석 - 동질성 검정 survey_method.csv
 
 #귀무 : 교육방법에 따른 교육생들의 만족도에 차이가 없다.
 #대립 : 교육방법에 따른 교육생들의 만족도에 차이가 있다
 
import pandas as pd
import  scipy.stats as stats
from anal5.test4chi import chi_result
 
data = pd.read_csv('../testdata/survey_method.csv')
print(data.head(5))
print(data['method'].unique()) #[1 2 3]
print(data['survey'].unique()) #[1 2 3 4 5]

ctab = pd.crosstab(index = data['method'], columns=data['survey'])
ctab.columns = ['매우만족','만족','보통','불만족','매우불만족']
ctab.index = ['방법1','방법2','방법3']
print(ctab)

chi2,p,ddof,_ =stats.chi2_contingency(ctab)
print('chi2,p,ddof :', chi2,p,ddof)
#해석 : p-value 0.58645 >0.05 이므로 귀무채택. 교육방법에 따른 교육생들의 만족도 차이가 없다.
# 조사된 관찰값은 우연히 발생했다고 할 수 있따. 

print('***'*30)
'''
동질성 검정 실습2> 연령대별 sns 이용률의 동질성 검정
20대에서 40대까지 연령대별로 서로 조금씩 그 특성이 다른 sns 서비스들에 대해 이용 현황을 조사한 자료를 바탕으로 연령대별로 홍보
전략을 세우고자 한다. 연령대별로 이용 현황이 서로 동일한지 검저해 보도록 하자
'''
# 귀무 :연령대별로 sns서비스들에 대한 이용 현황은 동일하다. (동질이다. 유사하게 분포되어 있다.)
# 대립 : 연령대별로 SNS서비스 ㅌㄹ에 대해 이용 현황은 동일하지 않다.

data = pd.read_csv('../testdata/snsbyage.csv')
print(data.head(3))
print(data.age.unique())
print(data.service.unique())
ctab = pd.crosstab(index=data.age, columns=data.service)
print(ctab)

#chi_result = [ctab.loc[1],ctab.loc[2],ctab.loc[3]]
chi2,p,ddof,_ = stats.chi2_contingency(chi_result)
print('chi2,p,ddof :', chi2, p, ddof)
#해석 : p-value 1.116790642 < 0.05 이므로 귀무가설 기각
#연령대별로 SNS 서비스들에 대해 이용 현황은 동일하지 않다. 조사된 자료는 우연히 발생한 것이 아니다

print()
#참고로 snsbyage.csv는 표본 데이터지만, 모집단이라 강정하고 표본을 추출해 처리해 보기
sample_data = data.sample(n=500,replace = True, random_state=1)
print(sample_data.head(3),' ',len(sample_data))

ctab2 = pd.crosstab(index=sample_data.age, columns=sample_data.service)
print(ctab2)

chi2, p,ddof,_ = stats.chi2_contingency(ctab2)
print('chi2,p,ddof :', chi2, p, ddof)
#귀무가설 기각
