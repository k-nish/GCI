#coding: utf8
import mysql.connector
import config
import csvkit

dbcon = mysql.connector.connect(database=config.db, user=config.user, password=config.passwd, host=config.host)
dbcur = dbcon.cursor()

# dataset = [
#     ('138297393', '38979', "^_^"),
#     ('298379847', '38979', "(-  - ;)"),
#     ('928398329', '88298',"((o_o;;;))))"),
#     ('382809389', '113918',"m(__)m"),
# ]
csv_data = csvkit.reader(file('rating_final.csv'))
for row in csv_data:
#複数データの追加
# for datas in dataset:
	# sql = ("INSERT INTO `tweets`(`tweet_id`, `user_id`, `tweet_text`) VALUES (%s,%s,%s)")
	sql = ("INSERT INTO `rating_final`(`userID`, `placeID`, `rating`, `food_rating`, `service_rating`) VALUES (%s,%s,%s,%s,%s)")
	dbcur.execute(sql, row)

#実際にMySQLに反映させる
dbcon.commit()

dbcur.close()
dbcon.close()

