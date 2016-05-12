#coding: utf8
UR = []
for i in range(1900, 2201):
    if i%400 == 0:
        UR.append(i)
    elif i%100 != 0 and i%4 == 0:
        UR.append(i)
for j in UR:
    print j
