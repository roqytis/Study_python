import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble._forest import RandomForestClassifier

df= pd.read_csv('winequality-red.csv')

from sklearn.model_selection import train_test_split
df_x = df.drop(columns = 'quality')
df_y = df['quality']
print(df_x.head())

# train / test
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)

# Model
model = RandomForestClassifier(criterion = 'entropy', n_estimators = 500)
model.fit(train_x, train_y)

# pred
pred = model.predict(test_x)

# acc
from sklearn.metrics import accuracy_score
print('acc : ', accuracy_score(test_y, pred))

print()
print('특성(변수) 중요도 : {}'.format(model.feature_importances_))
# [0.07141083 0.09889478 0.08055513 0.06815284 0.07765116 0.05703985
#0.09570376 0.08574203 0.07245264 0.12458179 0.16781517]

# 독립변수 중 중요 변수 확인
print()
import matplotlib.pyplot as plt
import numpy as np
print('특성(변수) 중요도 : {}' .format(model.feature_importances_))

def plot_importance_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align = 'center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel('attr importance')
    plt.ylabel('attr')
    plt.show()

plot_importance_func(model)