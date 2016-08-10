#coding: utf8
import mysql.connector
import config
import csvkit

dbcon = mysql.connector.connect(database=config.db, user=config.user, password=config.passwd, host=config.host)
dbcur = dbcon.cursor()

sql1 = "drop table if exists rating;"
dbcur.execute(sql1);
print "table削除"

sql2 = "create table rating (userID text, placeID int, rating int, food_rating int, service_rating int);"
dbcur.execute(sql2);
print "table作成"

csv_data = csvkit.reader(file('rating_final.csv'))
for row in csv_data:
	sql = "INSERT INTO `rating`(`userID`, `placeID`, `rating`, `food_rating`, `service_rating`) VALUES (%s,%s,%s,%s,%s)"
	dbcur.execute(sql, row)

#実際にMySQLに反映させる
dbcon.commit()

dbcur.close()
dbcon.close()

