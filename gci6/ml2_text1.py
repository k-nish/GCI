# coding: UTF-8
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