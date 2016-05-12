#coding: utf8
data = [
    {"name": "田中花子", "gender": "女性", "score": 58, "year" :1980},
    {"name": "鈴木一郎", "gender": "男性", "score": 76, "year" :2000},
    {"name": "山田太郎", "gender": "男性", "score": 69, "year" :1989},
    {"name": "佐藤恵子", "gender": "女性", "score": 62, "year" :1992},
    {"name": "石井あや", "gender": "女性", "score": 71, "year" :1978}
]

def avg(x):
    return 1.0 * sum(x) / len(x)

UR = []
for datum in data:
    if datum["year"]%400 == 0:
        UR.append(datum["score"])
    else:
        if datum["year"]%100 != 0:
            if datum["year"]%4 == 0:
                UR.append(datum["score"])

print "閏年に生まれた観客の平均評価点数は" + str(avg(UR))

NUR = []
for datum in data:
    if datum["year"]%400 != 0:
        if datum["year"]%100 == 0:
            NUR.append(datum["score"])
        else:
            if datum["year"]%4 != 0:
                NUR.append(datum["score"])

print "閏年以外の年に生まれた観客の平均評価点数は" + str(avg(NUR))