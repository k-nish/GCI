# coding: UTF-8
# gci:machine-leaning1の演習1の答え
import numpy as np
# 1.4×5次元の配列を生成
A = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6],[7,8,9,0]]
# numpy配列に変換
A = np.array(A)
print '1の出力'
print A

# 2.2列目、3行目を出力
a1 = A[:,2]
a2 = A[2]
print '2列目の表示'
print a1
print '3列目の表示'
print a2

# 3.3列目までとそれ以降で分割
X = A[:,0:3]
Y = A[:,3:]
print 'Xの表示'
print X
print 'Yの表示'
print Y

# 4.Xの各要素の中で平均より小さいものは-1,平均より大きいものは100と置き換える
avg = X.mean()
X[np.where(X<avg)] = -1
X[np.where(X > avg+3)] = 100
print '置換したXの表示'
print X

print X.shape
print Y.shape

# 5.Xとyを結合して元の配列と同じ大きさに戻す
# Y = np.reshape(Y,(5,1))
Z = np.hstack((X,Y))
print 'Zの表示'
print Z
print Z.shape
print Z[:,3]