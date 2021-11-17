import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pandas import Series, DataFrame

data = {"국어": [80, 90, 70, 30], "영어": [90, 70, 60, 40], "수학": [90, 60, 80, 70]}
columns = ["국어", "영어", "수학"]
df = DataFrame(data, columns=columns)
print(df)
print(data["수학"])

Total = df["수학"].sum()
print(Total/4)

#fr = DataFrame(data)
#print(fr)
