#coding: utf8
import numpy as np
import matplotlib
matplotlib.use("PDF") #PDFをAggにすればpngファイルにして保存できる
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

a=np.random.random((100,2))+2
b=np.random.random((100,2))+5
c=np.random.random((100,2))+8
X=np.concatenate((a,b,c))

k_means= KMeans(init='random', n_clusters=3) #init:初期化手法、n_clusters=クラスタ数を指定
k_means.fit(X)
Y=k_means.labels_ #得られた各要素のラベル

plt.figure(figsize=(10,5))
plt.scatter(*zip(*X), c= k_means.labels_, vmin=0, vmax=2, s=12)

plt.savefig("class2.pdf")
# plt.show()
