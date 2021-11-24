# 많은 양의 데이터를 이용해 데이터 분석을 하고 싶으나 구하지 못했다면 직접 만들 수 있다.
# 비만도 측정(BMI지수 : 체질량 지수) = 몸무게 (kg) / (키 (m) * 키 (m))   체중 / 키의 제곱
# print(65 / ((175/100) * (175 / 100)))
# 18.5 미만 : 저체중, 18.5 이상 ~ 23.0 미만이면 정상, 23.0 이상이면 비만

# 체질량 지수를 사용하여 원하는 크기 만큼의 파일 작성
import random

def calc_bmi(h, w):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5: return 'thin'
    elif bmi < 23.0: return 'normal'
    else: return 'fat'

# print(calc_bmi(170, 80))
#
# # 파일로 작성
# fp = open('bmi.csv', 'w', encoding = 'UTF-8')
# fp.write('height,weight,label\n')
#
# # 무작위로 생성
# cnt = {'thin' : 0, 'normal':0, "fat": 0} # dict type
# for i in range(50000):
#     h = random.randint(150, 200) # 키
#     w = random.randint(35, 100) # 몸무게
#     label = calc_bmi(h, w)
#     cnt[label] += 1
#     fp.write('{0},{1},{2}\n'.format(h,w, label))
#
# fp.close()
# print('ok')

# BMI data로 SVM 모델 작성
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv('bmi.csv')
print(tbl[:3], ' ', tbl.shape)  # (50000, 3)

# 정규화 : 0 ~ 1 사이 값으로 표현
w = tbl['weight'] / 100
h = tbl['height'] / 200
wh = pd.concat([w, h], axis = 1)
label = tbl['label']
label = label.map({'thin' : 0, 'normal':1, "fat": 2})
print(wh.head(3)) 
 
# train / test
data_train, data_test, label_train, label_test = train_test_split(wh, label)
print(data_train[:2], ' ', data_train.shape) 
print(data_test[:2], ' ', data_train.shape) 
print(label_train[:2], ' ', data_train.shape) 
print(label_test[:2], ' ', data_train.shape) 

# 모델 작성
model = svm.SVC(C = 0.1).fit(data_train, label_train)

pred = model.predict(data_test)  # 모델 검정은 test data를 사용
print('실제값 : ', label_test[:10].values)
print('예측값 : ', pred[:10])

acc_scsore = metrics.accuracy_score(label_test, pred)
print('분류 정확도 : ', acc_scsore)

print()
cl_report = metrics.classification_report(label_test, pred)
print('분류 보고서 : ', cl_report)

# 시각화
tbl2 = pd.read_csv('bmi.csv', index_col = 2)
print(tbl2.head(3))

def scatter_func(lbl, color):
    b = tbl2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label = lbl)
    
scatter_func('thin', 'red')
scatter_func('normal', 'yellow')
scatter_func('fat', 'blue')
plt.legend()
plt.show()