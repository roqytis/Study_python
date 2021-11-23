# 국내 관광지(5개)에 대해 외국인(미국, 일본, 중국) 방문 상관관계 분석

import json
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import pandas as pd


# scatter graph 작성 함수
def setScatterGraph(tour_table, all_table, tourpoint):
    # 계산할 관광지명에 해당하는 데이터만 추출해 변수에 저장하고, 외국인 자료와 병합
    tour = tour_table[tour_table['resNm'] == tourpoint]
    # print("tour: ", tour)
    merge_table = pd.merge(tour, all_table, left_index=True, right_index=True)
    print("merge_table: ", merge_table)
    

def chulbalFunc():
    # 서울 관광지 파일 읽어 DataFrame에 저장
    fname = '../testdata/서울특별시_관광지입장정보_2011_2016.json'
    jsonTp = json.loads(open(fname, 'r', encoding='UTF-8').read())  # str -> dict : json decoding
    tour_table = pd.DataFrame(jsonTp, columns=("yyyymm", "resNm", "ForNum"))  # 년월일, 관광지명, 입장객수
    tour_table = tour_table.set_index("yyyymm")
    # print(tour_table)  # 201101        창덕궁   14137 ...
    
    # 관광지 이름 얻기
    resNm = tour_table.resNm.unique()
    # print('resNm: ', resNm)  # ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘' '국립중앙박물관' '서울역사박물관'...

    """-----------------------------------------------------------------------------------------------"""

    # 중국인 자료를 읽어 DataFrame에 저장
    cdf = '../testdata/중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding='UTF-8').read())
    china_table = pd.DataFrame(jdata, columns=("yyyymm", "visit_cnt"))
    china_table = china_table.rename(columns={"visit_cnt":"china"})
    china_table = china_table.set_index("yyyymm")
    print(china_table[:2])
    
    # 일본인 자료를 읽어 DataFrame에 저장
    jdf = '../testdata/일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding='UTF-8').read())
    japan_table = pd.DataFrame(jdata, columns=("yyyymm", "visit_cnt"))
    japan_table = japan_table.rename(columns={"visit_cnt":"japan"})
    japan_table = japan_table.set_index("yyyymm")
    print(japan_table[:2])
    
    # 일본인 자료를 읽어 DataFrame에 저장
    udf = '../testdata/미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding='UTF-8').read())
    usa_table = pd.DataFrame(jdata, columns=("yyyymm", "visit_cnt"))
    usa_table = usa_table.rename(columns={"visit_cnt":"usa"})
    usa_table = usa_table.set_index("yyyymm")
    print(usa_table[:2])
    
    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    
    r_list = []
    for tourpoint in resNm[:5]:
        setScatterGraph(tour_table, all_table, tourpoint)
        

if __name__ == '__main__':
    chulbalFunc()
