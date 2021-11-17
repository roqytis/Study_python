# seaborn으로 matplotlib 의 기능을 향상

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.info())

sns.displot(titanic['age'])
plt.show()

sns.boxplot(y='age', data=titanic, palette='Paired')
plt.show()

sns.relplot(x='who', y='age', data=titanic)
plt.show()

# sns.countplot(x='class',data=titanic)
sns.countplot(x='class', data=titanic, hue='who')
plt.show()

ti_pivot = titanic.pivot_table(index='class', columns='sex', aggfunc='size')
print(ti_pivot)
sns.heatmap(ti_pivot, cmap=sns.light_palette('gray', as_cmap=True), annot=True, fmt='d')
plt.show()

# pandas의 시각화 기능
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 3), index=pd.date_range('1/1/2000', periods=10), columns=['a', 'b', 'c'])
print(df.tail(5))
df.plot()
#df.plot(kind='bar')
#df.plot(kind='box')
plt.xlabel('time')
plt.ylabel('data')
plt.show()

df[:5].plot.bar()
plt.show()


