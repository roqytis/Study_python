# 공분산, 상관계수
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../testdata/drinking_water.csv')
print(data.head(3))

print()
# 공분산 // 회귀분석 전 단계로 상관분석
print(np.cov(data.친밀도, data.적절성))
print(np.cov(data.친밀도, data.만족도))
print()
print(data.cov())

print()
# 상관계수 // 회귀분석 전 단계로 상관분석
print(np.corrcoef(data.친밀도, data.적절성))
print(np.corrcoef(data.친밀도, data.만족도))
print()
print(data.corr())
print(data.corr(method='pearson')) # spearman, kendall

# 시각화
# data.plot(kind='scatter', x='만족도', y='적절성')
# plt.show()
#
# from pandas.plotting import scatter_matrix
# attr = ['친밀도', '적절성', '만족도']
# scatter_matrix(data[attr], figsize=(10, 6))
# plt.show()

# hitmap
import seaborn as sns
sns.heatmap(data.corr())
plt.show()

# hitmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()