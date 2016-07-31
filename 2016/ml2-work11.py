# coding: UTF-8
# Fashionカテゴリの製品を買うかどうかの予測の精度を向上させる
# 仮説3:Fashionカテゴリ、Miscellaneousカテゴリ、Travel_Sportsカテゴリ、Entertainmentカテゴリの購買行動を注文したデータ6ヶ月分のみを用いると精度は向上する
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score
import pandas as pd
import numpy as np

# column取得
data = pd.read_csv('gci_Feature_user1000.csv')
columns = data.columns
print 'columns取得'
print columns

columns = data.columns
for col in columns:
	col_list = col.split('_')
	# if 'PA' not in col_list:
	# 	columns = columns.drop(col)
	if 'Fashion' not in col_list and 'Travel' not in col_list :
		columns = columns.drop(col)

print 'columns'
print columns

data = data.ix[:,columns]

X = data.ix[:,'PA_Fashion_1month_ago': 'PA_Travel_Sports_4month_ago']
y = data.ix[:,'Is_PA_Fashion']

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1234)
clf = RandomForestClassifier(random_state =1234)
# training
clf.fit(train_X, train_y)
# prediction
y_hat = clf.predict(test_X)
# result
print '仮説の検証'
print y_hat
print precision_score(test_y, y_hat)

# 仮説3:Fashion6,Miscellaneous6,Travel6,Entertainment6→0.620218579235
# 仮説4:Fashion6,travel6→0.638054363376
# 仮説5:Fashion6, travel6, kids_baby6→0.627814569536
# 仮説6:fashion6,travel6, health6→0.620786516854
# 仮説7:fashion6, travel6, teens6→0.618571428571
# 仮説8:fashion6,travel6,Other6→0.627142857143
仮説9:fashion6,travel4→0.640513552068
