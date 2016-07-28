# coding: UTF-8
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score

from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

digits = load_digits(n_class=10)
X, y = digits.data, digits.target

#訓練データとテストデータが8:2になるように分割
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)
# 学習器を作る
clf = LogisticRegression()
# training
clf.fit(train_X, train_y)
# 予測
pred = clf.predict(test_X)
print pred
pred_proba = clf.predict_proba(test_X)
print pred_proba[:10]
# 結果表示
print 'ロジスティック回帰による予測結果'
print (precision_score(test_y, pred))

clf2 = RandomForestClassifier(random_state = 28)
# training
clf2.fit(train_X, train_y)
# prediction
pred2 = clf2.predict(test_X)
print 'ランダムフォレストによる予測結果'
print (precision_score(pred, test_y))

# データをnumpy配列に変換する
X = np.array(X, dtype="float32")
y = np.array(y, dtype="float32")
X_np = X.astype(np.float32)
y_np = y.astype(np.float32)
# MinMaxScalerを用いてデータを変形する
scaler = MinMaxScaler()
MinMax_X = scaler.fit_transform(X_np)
MinMax_y = scaler.fit_transform(y_np)

#訓練データとテストデータが8:2になるように分割
train_X, test_X, train_y, test_y = train_test_split(MinMax_X, MinMax_y, test_size=0.2, random_state=1234)
# 学習器を作る
clf = LogisticRegression()
# training
clf.fit(train_X, train_y)
# 予測
pred = clf.predict(test_X)
print pred
pred_proba = clf.predict_proba(test_X)
print pred_proba[:10]
# 結果表示
print 'データ正規化後のロジスティック回帰による予測結果'
print (precision_score(test_y, pred))

clf2 = RandomForestClassifier(random_state = 28)
# training
clf2.fit(train_X, train_y)
# prediction
pred2 = clf2.predict(test_X)
print 'データ正規化後のランダムフォレストによる予測結果'
print (precision_score(pred, test_y))



