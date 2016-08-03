# coding: UTF-8
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split,StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.grid_search import GridSearchCV
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target

params = {'C':[0.01, 0.1, 1.0, 10], 'penalty':['l1','l2']}
lr = LogisticRegression()
clf = GridSearchCV(lr, params)

# params = 
skf = StratifiedKFold(y, n_folds = 3)
for train_index, test_index in skf:
	train_X, test_X = X[train_index], X[test_index]
	train_y, test_y = y[train_index], y[test_index]
	print train_X.shape
	print test_X.shape
	print train_y.shape
	print test_y.shape
