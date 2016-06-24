# グラフ描画用のライブラリロード
%matplotlib inline
import matplotlib.pyplot as plt

# データベース接続のコネクターをimport
import mysql.connector
# データベース接続情報をダウンロード
from local_config import mariadb_config
# データベースに接続
mariadb_config["database"] = "gci"
db = mysql.connector.connect(**mariadb_config)
#db = mysql.connector.connect(user="root", password="xxxx", database="gci")
cursor = db.cursor()

cursor.execute("select HH_ID, OrderNum, Dollars from Orders where HH_ID=1")
row = cursor.fetchone()
while row is not None:
	print (row[0],row[1],row[2])
	row = cursor.fetchone()
cursor.close()
db.close()


# cursorをcloseするとそのcursorはもう使えない
# contextlibのclosingとwith文を組み合わせてcursorを自動的にcloseする
from contextlib import closing
db = mysql.connector.connect(**mariadb_config)
with closing(db.corsor()) as cur:
	cur.execute("select * from Household order by HH_ID limit 10")
	row = cur.fetchone
	while row is not None:
		print (row[0],row[1])
		row = cur.fetchone
db.close()


# ZIPDescriptionテーブルから州名降順に10個レコードを取ってきてprintする
db = mysql.connector.connect(**mariadb_config)
with closing(db.cursor()) as cur:
	cur.execute("select ZIPCode, state from ZIPDescription order by state desc limit 10")
	row = cur.fetchone()
	print row
	while  row is not None:
		print (row[0],row[1])
		row = cur.fetchone()
db.close()

# クエリに変数を使いたいとき
with closing(db.cursor()) as cur:
	hh_id = 3
	cur.execute("select * from Orders where HH_ID = %s", (hh_id,))
	row.cur.fetchone()
	while row is not None:
		print row
		row = cur.fetchone()
db.close()
# executeの2番目の引数はタプルなので(hh_id)ではタプルとして認識されずにエラーとなるので注意


# グラフの描画
statement = """select Dollars from Orders where HH_ID = 32896 """
y = []
with closing(db.cursor()) as cur:
	cur.execute(statement)
	row = cur.fetchone
	while row is not None:
		y.append(int(row[0]))
		row = cur.fetchone()
# hist()を用いて描画する
_ = plt.hist(y, bins=20)


# 年ごとのログをとる
statement = """select HH_ID,sum(OrderDate >= "20050101" and OrderDate <= "20051231") as "2005", sum(OrderDate >= "20060101" and OrderDate <= "20061231") as "2006", sum(OrderDate >= "20070101" and OrderDate <= "20071231") as "2007" from Orders where HH_ID <= 5 group by HH_ID;"""
X = ["2005", "2006", "2007"]
Ys = []
while closing(db.cursor()) as cur:
	cur.execute(statement)
	row = cur.fetchone()
	print row
	while row is not None:
		Ys.append(row)
		row = cur.fetchone()
db.close()
# plot()を用いて描画する
for Y in Ys:
	plt.plot(X, Y[1,:], label=Y[0])
plt.legend()

# 演習問題
# HH_IDが32896のユーザについて、月ごとの購入数のグラフを作成する
# ・case文ではなくpythonのfor文にて作成する


# 1回の購入金額あたりの分布を作成する
# ヒストグラム作成はplt.hist()で作成できる。単純にplt.hist()をするとレコード数が多すぎるのでSQLで適当な範囲ごとのレコード数を計算し、プロットしたほうがよい

