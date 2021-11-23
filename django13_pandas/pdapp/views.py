from django.shortcuts import render
from pdapp.models import Jikwon
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def dispFunc(request):
    datas = Jikwon.objects.all().values()
    # print(datas)
    df = pd.DataFrame.from_records(datas)
    # pd.set_option('display.max_columns', 300) 모든 컬럼 나오게
    df.columns = ['사번', '직원명', '부서', '직급', '연봉', '입사', '성별', '평점']
    # print(df.head(3))
    ctab = pd.crosstab(df.성별, df.직급, margins=True)
    
    # 시각화
    buser_group = df['연봉'].groupby(df['부서'])
    print(buser_group)
    buser_group_detail = {'sum':buser_group.sum(), 'avg':buser_group.mean()}
    print(buser_group_detail)
    
    bu_result = buser_group.agg(['sum', 'mean'])
    bu_result.plot(kind='barh')
    plt.title('부서별 연봉합, 연봉평균')
    fig = plt.gcf()
    fig.savefig('django13_pandas/pdapp/static/images/test1.png')
    
    return render(request, 'list.html', {'datas' : df.to_html(), 'ctab':ctab.to_html(),
                                          'buser_group_detail':buser_group_detail})