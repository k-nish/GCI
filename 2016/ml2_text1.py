# coding: UTF-8
# gci授業:machine learning2の授業内容

#データ準備
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas as pd

data = pd.read_csv('gci_Feature_user1000.csv')
#上から5行だけ見てみる
print(data.ix[:5])

from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score

X = data.ix[:, 'PA_Electronics_1month_ago': 'PA_Unclassified2_6month_ago'].values
y = data.ix[:, 'Is_PA_Fashion'].values

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)

clf = RandomForestClassifier(random_state=123)
#training
clf.fit(train_X, train_y)
#prediction
y_hat = clf.predict(test_X)

#result
print(y_hat)
print(precision_score(test_y, y_hat))

#データ準備
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas as pd

data = pd.read_csv('gci_Feature_user1000.csv')
#上から5行だけ見てみる
#print(data.ix[:5])
columns = data.columns
for col in columns:
    col_list = col.split('_')
    if '4month' in col_list or '5month' in col_list or '6month' in col_list:
        columns = columns.drop(col)

print(columns)
data = data.ix[:, columns]

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score

X = data.ix[:, 'PA_Electronics_1month_ago': 'PA_Unclassified2_3month_ago'].values
y = data.ix[:, 'Is_PA_Fashion'].values

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)

clf = RandomForestClassifier(random_state=123)
#training
clf.fit(train_X, train_y)
#prediction
y_hat = clf.predict(test_X)

#result
print(y_hat)
print(precision_score(test_y, y_hat))

from sklearn.cross_validation import train_test_split
import numpy as np
import pandas as pd

data = pd.read_csv('gci_Feature_user1000.csv')
#上から5行だけ見てみる
#print(data.ix[:5])
columns = data.columns
for col in columns:
    col_list = col.split('_')
    if 'PA' in col_list and 'Is' not in col_list and 'Fashion' not in col_list:
        columns = columns.drop(col)

print(columns)
data = data.ix[:, columns]

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score

X = data.ix[:, 'PA_Fashion_1month_ago': 'PA_Fashion_3month_ago'].values
y = data.ix[:, 'Is_PA_Fashion'].values

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)

clf = RandomForestClassifier(random_state=123)
#training
clf.fit(train_X, train_y)
#prediction
y_hat = clf.predict(test_X)

#result
print(y_hat)
print(precision_score(test_y, y_hat))

# one-hot-encode
from sklearn.preprocessing import OneHotEncoder
# 1~2列目が数値、3~4列目がカテゴリ変数とする
# 与えらえたデータ中にはないが、3列目のカテゴリ変数は1~4,4列目は1~6とする
X = np.array([[12,3,4,6],[5,10,1,4],[9,3,2,2],[7,4,3,2]])
encoder = OneHotEncoder(n_values=[5,7],categorical_features=[2,3], sparse=False)

# これを用いると、カテゴリ変数が左、数値変数が右と順序が変えられてしまう
X = encoder.fit_transform(X)
print X

# 正規化
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

X = np.array([[12, 3, 4, 6], [5, 10, 1, 4], [9, 3, 2, 2], [7, 4, 3, 2]], dtype = 'float32')
print X
# 平均0, 標準偏差1になるように変換
scaler = StandardScaler()
# fit_transformで変換方法を算出し、適用
# transformでfitした結果を適用
standard_X = scaler.fit_transform(X)
print 'standard_X'
print standard_X

# 最大値1, 最小値0になるように変換
scaler = MinMaxScaler()
# fit_transformで変換方法を算出し、適用
# transformでfitした結果を適用
MinMax_X = scaler.fit_transform(X)
print 'MinMax_X'
print MinMax_X

# ノイズとなる特徴量を除く
# 一定の値の列を除く
X = np.array([[1,3,5],[2,3,3],[-1,3,4],[1,3,0]])
print X
# np.std():配列の列or行の標準偏差
# np.delete(array, obj, axis)で削除
print np.delete(X, np.where(np.std(X, axis=0)==0), 1)

# L1正則化
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target
print X.shape
clf = LogisticRegression(C=0.01, penalty="l1")
clf.fit(X,y)

model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
print X_new.shape

# 変更重要度による特徴選択
iris = load_iris()
X,y = iris.data, iris.target
print X.shape
clf = RandomForestClassifier()
clf.fit(X,y)
# 変数重要度を表示
print (clf.feature_importances_)

model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
print X_new.shape

# パラメータチューニング
# grid search
from sklearn.grid_search import ParameterGrid
iris = load_iris()
X, y = iris.data, iris.target

# trainデータを分割してvalidationデータをつくる
train_X, train_y, valid_X, valid_y = train_test_split(X, y, test_size = 0.2, random_state = 1234)
clf = RandomForestClassifier()

# 探索したいパラメータ
params = {'n_estimators': range(5,8), 'max_features':[0.8, 0.9, 1.0]}
param_grid = ParameterGrid(params)
# 探索したいパラメータのすべての組み合わせが得られている
print list(param_grid)

# cross_validationを行ってgridsearchを行う
# cross_validationを使ってgridsearchをする場合はGridSearchCVが使える

from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV

iris = load_iris()
X,y = iris.data, iris.target

params = {'C':[0.01, 0.1, 1.0, 10], 'penalty':['l1','l2']}
lr = LogisticRegression()
clf = GridSearchCV(lr, params)

skf = StratifiedKFold(y, n_folds=3)
for train_index, test_index in skf:
	train_X, testX = X[train_index], X[test_index]
	train_y, test_y = y[train_index], y[test_index]

# fitするとcross_validationの結果が最もよいパラメータがセットされた予測器を返す
clf.fit(train_X, train_y)
# 予測
clf.predict(test_X)

# ベストの結果が出たパラメータ
print clf.best_params_
# ベストスコア
print clf.best_score_





