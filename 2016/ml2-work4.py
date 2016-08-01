# coding: UTF-8
from sklearn.grid_search import ParameterGrid
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import roc_auc_score, precision_score
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target

# trainデータを分割してvalidationデータをつくる
train_X, valid_X, train_y, valid_y = train_test_split(X, y, test_size = 0.2, random_state = 1234)

# 探索したいパラメータ
params = {'n_estimators': range(5,8), 'max_features':[0.8, 0.9, 1.0]}
param_grid = ParameterGrid(params)
# 探索したいパラメータのすべての組み合わせが得られている
print list(param_grid)

# ans_feature = param_grid[0]['max_features']
# ans_estimators = param_grid[0]['n_estimators']
max_predition = 0
# ans = np.array([])
ans = []
for i in range(0,8):
	# 学習器の設定
	clf = RandomForestClassifier(n_estimators = param_grid[i]['n_estimators'], max_features = param_grid[i]['max_features'])
	# 学習
	clf.fit(train_X, train_y)
	# 予測
	pred = clf.predict(valid_X)
	# 予測結果の正確性
	prediction = float(precision_score(valid_y, pred))
	print prediction
	# 最も正確な時のパラメータを答えとする
	if prediction > max_predition:
		ans.append([param_grid[i]['max_features'], param_grid[i]['n_estimators'], prediction])

# numpy配列に変換
answer = np.array(ans)
# 精度が最大になるindexを取得
ans_i = np.argmax(answer, axis = 0)[2]
# 求めるパラメータの出力
print u"精度が最大になるmax_featuresは" + str(answer[ans_i][0])
print u"精度が最大になるn_estimatorsは" + str(answer[ans_i][1])
# 最もよいパラメータはfeature=0.8 esitimators = 5←間違いの模様
# predictionがすべて1になっているので評価できず。。。
