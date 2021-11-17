# 시각화 : matplotlib 모듈을 사용
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')  # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False  # 한글 깨짐 방지 때문에 음수 깨짐 을! 방지

x = ['서울', '인천', '수원']
# x = ('서울', '인천', '수원')
# x = {'서울', '인천', '수원'} # 이건 안됨 - set는 순서가 없기 때문에...

y = [5, 3, 7]

plt.xlim([-1, 3])
plt.ylim([0, 10])
# plt.yticks(list(range(0, 11, 3))) # y축의 간격을 자동에서 수동으로 수정
plt.plot(x, y)
plt.show()

print()
data = np.arange(1, 11, 2)
print(data)  # [1 3 5 7 9] # y 측에 값, x 축에 구간 으로 사용
plt.plot(data)  # y 축 값으로 사용. x 축은 자동으로 구간 값이 표시

x = [0, 1, 2, 3, 4]
for a, b in zip(x, data):  # 좌표 표시하기
    plt.text(a, b, str(b))

plt.show()

plt.plot(data)
for a, b in zip(x, data):  # 좌표 표시하기
    plt.text(a, b, str(b))
plt.plot(data, data, 'r')
for a, b in zip(data, data):  # 좌표 표시하기
    plt.text(a, b, str(b))
plt.show()

# 사인 곡선에 x, y 출력
x = np.arange(10)
y = np.sin(x)
print(x, y)

#plt.plot(x, y, 'bo')
plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.show()

# hold 명령: 복수의 plot 명령을 하나의 그림에 겹쳐서 보기
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10,5))
plt.plot(x,y_sin,c='r')
plt.scatter(x, y_cos)
plt.title('sine & cosine')
plt.xlabel('x축')
plt.ylabel('y축')
plt.legend(['sine','consine'])
plt.show()

#subplot
plt.subplot(2,1,1)
plt.plot(x, y_sin)
plt.title('sine')

plt.subplot(2,1,2)
plt.plot(x, y_cos)
plt.title('consine')
plt.show()

#꺽은선 그래프 2개
irum = ['a', 'b', 'c', 'd', 'e']
kor = [80,50,70,70,90]
eng = [60,70,80,70,60]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bs-.')
plt.ylim([0,100])
plt.legend(['국어','영어'], loc = 4)
plt.grid()

fig = plt.gcf() #차트를 이미지로 저장 준비
plt.show()
fig.savefig('test.png')

#이미지 일기
from matplotlib.pyplot import imread
img = imread('test.png')
plt.imshow(img)
plt.show()