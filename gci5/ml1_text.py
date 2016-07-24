# coding: UTF-8
import sys

# データ準備
from sklearn.datasets import load_digits
digits = load_digits(n_class=10)
X, y = digits.data, digits.target
print X.shape
print y.shape
# (1797, 64)
# (1797,)

# データ分割
from sklearn.cross_validation import train_test_split
#訓練データとテストデータが8:2になるように分割
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)
print train_X.shape
print train_y.shape
# (1437, 64)
# (1437,)

# 学習(LogisticRegression)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, precision_score

clf = LogisticRegression()
# training
clf.fit(train_X, train_y)

# 予測
pred = clf.predict(test_X)
print pred

pred_proba = clf.predict_proba(test_X)
print pred_proba[:10]

# 結果表示
print test_y
print pred
print (precision_score(test_y, pred))

# ハイパーパラメータ
clf = LogisticRegression(C=0.1)
# training
clf.fit(train_X, train_y)
# prediction
pred = clf.predict(test_X)
# result
print (precision_score(test_y, pred))

# ランダムフォレスト
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score

clf = RandomForestClassifier(random_state = 28)
# training
clf.fit(train_X, train_y)
# prediction
pred = clf.predict(test_X)
print (precision_score(pred, test_y))

sys.exit(5)

