# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X
import pandas as pd
from sklearn.model_selection._split import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bodycheck.csv")
print(data.head(3), ' ', data.shape)   # (20, 6)

#데이터 셋 분할 
x = data[["게임","TV시청"]]
y = data.안경유무
print(set(y))  #{0, 1}
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 0)   
print(x_train.shape,x_test.shape)  # (14, 2) (6, 2)

# model 생성 하기
logi_model = LogisticRegression(C=10.0, random_state=0) 
print(logi_model)
result_logi = logi_model.fit(x_train, y_train)   #학습
 
y_pred = logi_model.predict(x_test)      
print(y_pred)  
print(y_test)     
print("예측값: ", y_pred)
print("실제값: ", y_test)
print("총 갯수: %d, 예측오류 수: %d"%(len(y_test),(y_test != y_pred).sum()))

print("정확도 : %.3f" %accuracy_score(y_test,y_pred))

# confusion_matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred, labels = [0, 1]))  # [1, 0]도 상관없음

# 입력 받은 새로운 값으로 예측하기
tmp1 = int(input("게임 시간 입력 :"))  
tmp2 = int(input("TV 시청 시간 입력:")) 

# predict() 함수로 결과 예측 --------------
predData = pd.DataFrame({'게임':[tmp1],'TV':[tmp2]})
y_pred = logi_model.predict(predData)[0]
print('y_pred : ', y_pred)
result = ''
if y_pred == 0:
    result = "안경착용 X"
elif y_pred == 1:
    result = "안경착용 O"

print("게임시간이  %d시간이고  TV시청시간이 %d시간인 사람의 안경착용여부는: %s" %(tmp1,tmp2,result)) 
