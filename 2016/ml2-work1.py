# coding: UTF-8
# Fashionカテゴリの製品を買うかどうかの予測の精度を向上させる
# 仮説1:Fashionカテゴリの購買行動とMiscellaneousカテゴリの購買行動を注文したデータ6ヶ月分のみを用いると精度は向上する
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score
import pandas as pd
import numpy as np

# column取得
data = pd.read_csv('gci_Feature_user1000.csv')
# columns = data.columns
# print 'columns取得'
# print(columns)

columns = data.columns
for col in columns:
	col_list = col.split('_')
	# if 'PA' not in col_list:
	# 	columns = columns.drop(col)
	if 'Fashion' not in col_list and 'Miscellaneous' not in col_list:
		columns = columns.drop(col)

# print 'columns'
# print columns

data = data.ix[:,columns]

X = data.ix[:,'PA_Fashion_1month_ago': 'PA_Miscellaneous_6month_ago']
y = data.ix[:,'Is_PA_Fashion']

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)
clf = RandomForestClassifier(random_state =1234)
# training
clf.fit(train_X, train_y)
# prediction
y_hat = clf.predict(test_X)
# result
print y_hat
print precision_score(test_y, y_hat)

# 精度は0.631728045326となり、Fashionの購買行動しか用いていなかった分析よりも精度が高くついた。すなわち、仮説1が正しいことを示すことができた。
