# 자연 언어는 사람들이 일상적을 쓰는 언어를 인공적으로 만들어진 언어인 인공어와 구분하여 부르는 개념이다.
# 자연어(corpus)를 토큰화 해서 단어를 수치로 표현하며 분류 예측 작업 가능

# 워드 임베딩(Word Embedding) :단어를 벡터로 표현하는 방법
# 1) 희소 표현(Sparse Representation) : 원-핫 인코딩, 리이블 인코딩
# 원- 핫 인코딩 : 단어의 인덱스의 값만 1이고, 나머지 인덱스에는 전부 0으로 표현되는 벡터 표현 방법
#  Ex) 강아지= [0 0 0 0 1 0 0 0 0 0 0 0 ...wndfir...0]

# 2) 밀집 표현(Dense Representation)
# 사용자가 설저한 값으로 모든 단어의 벡터 표현의 차원을 맞춥니다. 또한, 이과정에서 더이상 0과 1만 가진 갑이 아니라 실수값을 가지게 됩니다. 
# Ex) 강아지 = [0.2 1.8 1.1 -2.1 1.1 2.8 ...wndfir ...] #이 벡터의 차원은 128

import numpy as np
#원-핫 인코딩: 단어를 희소표현으로 구분, 단어가 많아 질수록 벡터의 크기가 커지고, 단어의 유사성을 파악할 수 없다.

data_list = ['python','lan','program','computer','say']

values = []
for x in range(len(data_list)):
    values.append(x)

#print(values)

one_hot = np.eye(len(values))
print(one_hot,' ',type(one_hot),' ',np.shape(one_hot))

#워드투벡터(Word2Vec) : 단어의 의미를 다차원 공간에 벡터화. 단어 사이의 관계를 표현 가능
from gensim.models import word2vec

sentence =[['python','lan','program','computer','say']]
model = word2vec.Word2Vec(sentence, min_count=1, vector_size=50)#Word2Vec(대상문자여, 단어빈도수제한, 차원수)
print(model)
print(model.wv)
word_vectors = model.wv
print('word_vector : ', word_vectors)
print()
print(word_vectors.key_to_index) #{'say': 0, 'computer': 1, 'program': 2, 'lan': 3, 'python': 4}
print(word_vectors.key_to_index.keys())
print(word_vectors.key_to_index.values())

vocabs = word_vectors.key_to_index.keys()
word_vector_list = [word_vectors[v] for v in vocabs]
print(word_vector_list[0])
print(len(word_vector_list[0]))

print()
print(model.wv.most_similar(positive = 'computer')) #-1 ~ 0 ~ 1 벡터 간에 유사(거리가 가까움)

#시각화
import matplotlib.pyplot as plt

def plot_2d(vocabs, xs, ys):
    plt.figure(figsize=(8,6))
    plt.scatter(xs, ys)
    for i , v in enumerate(vocabs):
        plt.annotate(v, xy=(xs[i], ys[i]))
        
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
xys = pca.fit_transform(word_vector_list)
xs = xys[:, 0]
ys = xys[:, 1]
plot_2d(vocabs, xs, ys)
plt.show()
