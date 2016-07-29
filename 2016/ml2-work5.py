# coding: UTF-8
from sklearn.cross_validation import StratifiedKFold
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target

skf = StratifiedKFold(y, n_folds=3)
# 予測精度を要素とするnumpy配列を宣言
ans = np.array([])
# cross_validationを行う
for train_index, test_index in skf:
    train_X,test_X = X[train_index], X[test_index]
    train_y,test_y = y[train_index], y[test_index]
    # 学習器の設定
    clf = RandomForestClassifier()
    # 学習
    clf.fit(train_X,train_y)
    # 予測
    pred = clf.predict(test_X)
    # 予測精度を計算
    prediction = precision_score(test_y, pred)
    # 予測をnumpy配列に入れる
    ans = np.append(ans, prediction)

# 結果の出力
print 'ans'
print ans
print 'ans.mean()'
print ans.mean()