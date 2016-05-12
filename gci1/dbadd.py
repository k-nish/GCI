#coding: utf8
import mysql.connector
import config
import csvkit

dbcon = mysql.connector.connect(database=config.db, user=config.user, password=config.passwd, host=config.host)
dbcur = dbcon.cursor()

csv_data = csvkit.reader(file('rating_final.csv'))
for row in csv_data:
	sql = ("INSERT INTO `rating`(`userID`, `placeID`, `rating`, `food_rating`, `service_rating`) VALUES (%s,%s,%s,%s,%s)")
	dbcur.execute(sql, row)

#実際にMySQLに反映させる
dbcon.commit()

dbcur.close()
dbcon.close()

