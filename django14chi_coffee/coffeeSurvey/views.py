from django.shortcuts import render
from coffeeSurvey.models import Survey
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def surveyFunc(request):
    return render(request, 'survey.html')

def surveyProcess(request):
    # DB에 저장
    insertDataFunc(request)
    rdata = list(Survey.objects.all().values())
   
    
    # 데이터 분석
    df, result, ctab= dataAnalysisFunc(rdata)
    
    
    #시각화
    fig = plt.gcf()
    getn_group = df['co_survey'].groupby(df['genNum']).count()
    getn_group.index = ['스타벅스', '커피빈', '이디아', '탐앤탐스']
    getn_group.plot.bar(subplots=True, color=['cyan', 'green'], width=0.5)
    plt.xlabel('브랜드 명')
    plt.ylabel('선호 건수')
    plt.title('커피 브랜드별 선호 분포')
    fig.savefig('django14chi_coffee/coffeeSurvey/static/images/coffee.png') #이미지 파일로 저장할 경로

    return render(request, 'list.html',
                   {'ctab':ctab.to_html(), 'result':result, 'df':df.to_html(index = False)})
     
     
def insertDataFunc(request):
    #print(request.POST.get('gender'), ' ', request.POST.get('age'), ' ', request.POST.get('co_survey'))
    try:
        if request.method == 'POST':
            Survey(
                gender = request.POST.get('gender'),
                age = request.POST.get('age'),
                co_survey = request.POST.get('co_survey'),
            ).save()
        
    except Exception as e:
        print('err :',e)
    
    
def dataAnalysisFunc(rdata):
   # print('dataAnalysisFUnc:',rdata)
    # 귀무 : 성별에 따라 선호하는 커피브랜드에 차이가 있다.
    # 귀무 : 성별에 따라 선호하는 커피브랜드에 차이가 없다.
    df = pd.DataFrame(rdata)
    #df.dropna()
    df['genNum']=df['gender'].apply(lambda g:1 if g == '남' else 2)
    df['genNum']=df['co_survey'].apply(lambda c:1 if c == '스벅' else 2 if c == '커피빈' else 3 if c == '이디아' else 4)
    #print(df)
    #ctab = pd.crosstab(index=df['genNum'],columns=df['coNum'])
    ctab = pd.crosstab(index=df['gender'],columns=df['co_survey'])
    print(ctab)
    chi2,p, ddof,_= stats.chi2_contingency(ctab)
    print('chi2:{}, p{}, ddof:{} :'.format(chi2, p, ddof))
    
    if p > 0.05:
        results = "p값이 {0}이므로 성별에 따라 선호하는 커피브랜드에 차이가 없다(귀무)".format(p)
    else:
        results = "p값이 {0}이므로 성별에 따라 선호하는 키피브랜드에 차이가 있다(대립)".format(p)
        
    return df,results,ctab
    