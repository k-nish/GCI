# coding: UTF-8
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score

from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

digits = load_digits(n_class=10)
X, y = digits.data, digits.target
print 'X.shape'
print X.shape
# 学習器を作る
clf = RandomForestClassifier(random_state = 28)
# 訓練データとテストデータの分割
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)
clf.fit(train_X, train_y)
# 予測
pred = clf.predict(test_X)
pred_proba = clf.predict_proba(test_X)
print '予測結果(特徴量選択なし)'
print precision_score(test_y, pred)

# 一定の値の列を除く
X_new = np.delete(X, np.where(np.std(X, axis=0)==0), 1)
print 'X.shape'
print X.shape
# 訓練データとテストデータの分割
train_X, test_X, train_y, test_y = train_test_split(X_new, y, test_size=0.2, random_state=1234)
clf.fit(train_X, train_y)
# 予測
pred = clf.predict(test_X)
pred_proba = clf.predict_proba(test_X)
print '予測結果(一定値の列削除)'
print precision_score(test_y, pred)

# L1正則化
lr = LogisticRegression(penalty = "L1")
lr.fit(X, y)
model = SelectFromModel(lr, prefit=True)
X_new = model.transform(X)
print 'X_new.shape'
print X_new.shape
# 訓練データとテストデータの分割
train_X, test_X, train_y, test_y = train_test_split(X_new, y, test_size=0.2, random_state=1234)
clf.fit(train_X, train_y)
# 予測
pred = clf.predict(test_X)
pred_proba = clf.predict_proba(test_X)
print '予測結果(L1正則)'
print precision_score(test_y, pred)

# 特徴量選択を行う
clf.fit(X_new, y)
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X_new)
print 'X_new.shape'
print X_new.shape
# 訓練データとテストデータの分割
train_X, test_X, train_y, test_y = train_test_split(X_new, y, test_size=0.2, random_state=1234)
clf.fit(train_X, train_y)
# 予測
pred = clf.predict(test_X)
pred_proba = clf.predict_proba(test_X)
print '予測結果(L1正則&変数重要度)'
print precision_score(test_y, pred)

# メモ
# digitsのデータの中に一定値の列が存在しなかったので一定値の列削除は結果に影響を与えなかった
# L1正則化は精度向上に寄与した
# 特徴量選択だけでは精度は変化しなかった
