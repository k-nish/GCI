# coding: UTF-8
from sklearn.preprocessing import OneHotEncoder
import numpy as np
# 1~2列目が数値、3~4列目がカテゴリ変数とする
# 与えらえたデータ中にはないが、3列目のカテゴリ変数は1~4,4列目は1~6とする
X = np.array([[12,3,4,6],[5,10,1,4],[9,3,2,2],[7,4,3,2]])
encoder = OneHotEncoder(n_values=[5,7],categorical_features=[2,3], sparse=False)

# これを用いると、カテゴリ変数が左、数値変数が右と順序が変えられてしまう
X = encoder.fit_transform(X)
print X