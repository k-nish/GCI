#coding: UTF-8
import numpy as np
#3×4の行列を作成
A = [[1,2,3,4],[5,6,7,8],[9,0,1,2]]
A = np.array(A)
print '行列Aを表示'
print A

#課題2
print 'Aの1列目を表示'
print A[:,0]

print 'Aの2列目を表示'
print A[:,1]

#課題3
X = A[:,0:-1]
Y = A[:,-1]
print 'Xの表示'
print X

print 'Yの表示'
print Y

#課題4
avg = X.mean()
X[np.where(X>avg)] = 0
print '要素を変えたXの表示'
print X

#課題5
Y = np.reshape(Y,(3,1))
# Y = Y.T
Z = np.hstack((X, Y))
print 'XとYの結合Zの表示'
print Z
# print X.shape
# print Y.shape
# print Y