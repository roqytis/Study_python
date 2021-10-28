# numpy
# 배열에 행 또는 열추가
import numpy as np


aa = np.eye(3)
print(aa)

bb = np.c_[aa, aa[2]]
print('bb: \n', bb)

cc = np.r_[aa, [aa[2]]]
print('cc: \n', cc)

print()
a = np.array([1,2,3])
print(a)
b = np.append(a,[4,5])
print(b)
c = np.insert(a, 0, [6,7])
print(c)
d = np.delete(a, 1)
print(d)

# 조건 연산
x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
result = np.where(conditionData,x,y)
print(result)

print()
aa = np.where(x >= 3)
print(aa)
print(x[aa])

print('배열 결합, 분할')
kbs = np.concatenate([x,y])
print(kbs)
x1, x2 = np.split(kbs, 2)
print(x1)
print(x1)

print()
a = np.arange(1, 17).reshape(4, 4)
print(a)

x1,x2 = np.hsplit(a, 2) #좌우로 분리
print(x1)
print(x2)

x1,x2 = np.vsplit(a, 2) #상하로 분리
print(x1)
print(x2)

print('표본 추출 -- sampling : 복원, 비복원')
import random

li = np.array([1,2,3,4,5,6,7])
# 복원 추출
for _ in range(5):
    print(li[random.randint(0, len(li) - 1)], end=' ')

print()
# 비복원 추출
print(random.sample(list(li), k=5))

print('로또 번호')
print(random.sample(range(1, 46), k=6))  # 비복원

print()
print(list(np.random.choice(range(1, 46), 6)))  # 복원
print(list(np.random.choice(range(1, 46), 6, replace=False)))  # 비복원


print()
print('문제 풀어보기')
# * numpy의 array() 관련 연습문제 *
# 1) step1 : array 관련 문제
np.random.seed(12)
data = np.random.randn(5,4)
print(data)

i = 1
for row in data:
    print(i, '행 합계: ',row.sum())
    #print(i, '행 최댓값: ',row.max())
    
    print(i, '행 최댓값: ',np.max(row))
    i += 1
    
print(data.sum(axis = 1))
print(np.sum(data, axis = 1))
print(data.max(axis = 1))
   

print('문 2-1')   
#2) step2 : indexing 관련문제
print()
# 문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
zarr = np.zeros((6,6))
print(zarr)
#조건1> 36개의 셀에 1~36까지 정수 채우기
cnt = 0
for i in range(6):
    for j in range(6):
        cnt += 1
        zarr[i,j] = cnt
print(zarr)
#조건2> 2번째 행 전체 원소 출력하기 
#           출력 결과 : 7.   8.   9.  10.  11.  12.

print(zarr[1, :])

#조건3> 5번째 열 전체 원소 출력하기
#           출력결과 : 5. 11. 17. 23. 29. 35.
print(zarr[:, 4])

#조건4> 15~29 까지 블럭으로 출력하기
#           출력결과 : 
#           15.  16.  17.
#           21.  22.  23
#           27.  28.  29.
print(zarr[2:5, 2:5])

#문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
zarr = np.zeros((6,4))
print(zarr)
#     조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고, 두 번째 열부터는 1씩 증가시켜 원소 저장하기
ran = np.random.randint(20,100,6)
ran = list(ran)
print(ran)

for row in range(len(zarr)):
    num =ran.pop(0)
    for col in range(len(zarr[0])):
        zarr[row][col] = num
        num += 1
print(zarr)

zarr[0][:] = 1000
zarr[-1][:] = 6000
print(zarr)

print('---------------------------')
#3) step3 : unifunc 관련문제

#  표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후
#  아래와 같이 넘파이 내장함수(유니버설 함수)를 이용하여 기술통계량을 구하시오.
#  배열 요소의 누적합을 출력하시오.
arr = np.random.randn(4, 5)
print(arr)
print('평균: ', np.mean(arr))
print('합계: ', np.sum(arr))
print('표준편차: ', np.std(arr))
print('최댓값: ', np.max(arr)) #arr.min()
print('최솟값: ', np.min(arr))
print('1사분위 수: ', np.percentile(x,25))
print('2사분위 수: ', np.percentile(x,50))
print('3사분위 수: ', np.percentile(x,75))
print('요소값 누적합: ', np.cumsum(arr))