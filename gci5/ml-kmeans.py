# coding: UTF-8
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1,3], [2,3], [1,2], [0,2], [0,5], [0,6],[2,5]])
# k=3に設定
kmeans = KMeans(n_clusters=3)

kmeans.fit(X)
# 各データ点の所属するクラスタを表示
cluster_labels = kmeans.predict(X)
print cluster_labels

# 各クラスタの中心点
print kmeans.cluster_centers_