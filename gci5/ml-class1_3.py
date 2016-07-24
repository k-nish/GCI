# coding: UTF-8
# gradient boosting machineを用いた分析

import sys
import numpy as np
from sklearn import ensemble
from sklearn import datasets
from sklearn.metrics import precision_score

# データ準備
from sklearn.datasets import load_digits
digits = load_digits(n_class=10)
X, y = digits.data, digits.target
# print X.shape
# print y.shape

# データ分割
from sklearn.cross_validation import train_test_split
#訓練データとテストデータが8:2になるように分割
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)
# print train_X.shape
# print train_y.shape

# 学習
# パラメータを変えて実行する
# n_estimators=10000(default 100)としても精度は変わらなかった。0.973296096279のまま
# learning_rate=0.001とすると精度は0.860877766076
# learning_rate = 0.01とすると精度は0.898494309892
# learning_rate = 0.15とすると精度は0.975617078873
# learning_rate = 0.20とすると精度は0.980886229107
# learning_rate = 0.25とすると精度は0.973091826348
# learning_rate = 0.225とすると精度は0.978198057064
# learning_rate = 0.2125とすると精度は0.973629069555

# 以下learning_rateは0.20で行う
# max_depthを10とすると0.916587685344
# max_depthを1とすると0.946262484792
# max_depthを5とすると0.967159005869
# max_depthを2とすると0.981147186147
# max_depthを4とすると0.975648294689

clf = ensemble.GradientBoostingClassifier(learning_rate=0.2, max_depth=4)
clf.fit(train_X, train_y)

# 予測
pred = clf.predict(test_X)
# print 'pred'
# print pred

pred_proba = clf.predict_proba(test_X)
# print 'pred_proba'
# print pred_proba[:10]

# 結果表示
# print 'test_y'
# print test_y
# print 'pred'
# print pred
print 'precision_score'
print (precision_score(test_y, pred))
