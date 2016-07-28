from sklearn.cross_validation import StratifiedKFold
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

skf = StratifiedKFold(y, n_folds=3)
for train_index, test_index in skf:
    train_X,test_X = X[train_index], X[test_index]
    train_y,test_y = y[train_index], y[test_index]