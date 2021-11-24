# 결정 트리 학습법(decision tree learning)은 어떤 항목에 대한 관측값과 목표값을 연결시켜주는 예측 모델로서 결정 트리를 사용한다. 
# 이는 통계학과 데이터 마이닝, 기계 학습에서 사용하는 예측 모델링 방법 중 하나이다. 트리 모델 중 목표 변수가 유한한 수의 값을 가지는 것을 분류 트리라 한다.
# 이 트리 구조에서 잎(리프 노드)은 클래스 라벨을 나타내고 가지는 클래스 라벨과 관련있는 특징들의 논리곱을 나타낸다.
# 결정 트리 중 목표 변수가 연속하는 값, 일반적으로 실수를 가지는 것은 회귀 트리라 한다.

import pydotplus
from sklearn import tree
import collections

x = [[180,15],[177,42],[156,35],[174,5],[166, 33]]
y = ['man','woman','woman','man','woman']
label_names = ['height', 'hair_length']

model = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
print(model)

model.fit(x,y)
print('훈련 정확도 : ', model.score(x, y))
pred = model.predict(x)
print('예측값 : ', pred)
print('실제값 :', y)

#시각화
dot_data = tree.export_graphviz(model,
                                feature_names = label_names,
                                out_file = None, 
                                filled = True,
                                rounded = True)
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('red', 'orange')
edges = collections.defaultdict(list)

for e in graph.get_edge_list():
    edges[e.get_source()].append(e.get_destination())
    
for e in edges:
    edges[e].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[e][i]))[0]
        dest.set_fillcolor(colors[i])
        
graph.write_png('tree.png')

from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
img = imread('tree.png')
plt.imshow(img)
plt.show()