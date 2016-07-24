# coding: UTF-8
from sklearn.preprocessing import StandardScalar, MinMaxScalar
import numpy as np

X = np.array([[12,3,4,6],[5,10,1,4],[9,3,2,2],[7,4,3,2]],dtype='float32')
print X

# 平均0,標準偏差1になるように変換
scalar = StandardScalar()
# fit_transformで変換方法を導出し、適用
# transformでfitした結果を適用
standard_X = scalar.fit_transform(X)

print standard_X