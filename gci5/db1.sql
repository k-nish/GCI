-- サーバ内のデータベースを表示
show databases;
-- そのデータベースがあればデータベースを削除
drop database if exists TEST1;
-- TEST1というデータベースを作成
create database TEST1;

-- 使うデータベースを選択
use TEST1;
-- id[int]とname[varchar(20)]をもつテーブルを作成
create table meibo (id int primary key,name varchar(20)) engine = MyISAM,default charset = utf8;
-- meiboテーブルから全テーブルを取得
select * from meibo;
-- meiboにデータを追加
insert into meibo (id, name) values (1, "Yamada");
insert into meibo (id, name) values (2, "Tanaka");
insert into meibo (id, name) values (3, "Sato");

-- idが2のデータを取得
select * from meibo where id=2;
-- idが1か2のデータを取得
select * from meibo where id in (1,2);
-- idが2より大きいデータを取得
select * from meibo where id>2;
-- 名前がSから始めるデータを取得
select * from meibo where name like 'S%';
-- 名前がaで終わるデータを取得
select * from meibo where name like '%a';

-- meiboテーブルのデータ数を取得
select count(*) from meibo;
-- データ数のフィールド名をcountにしてデータ数を取得
select count(*) as count from meibo;
-- idの降順に全データを取得
select * from meibo order by id desc;

-- データの更新
update meibo set name = "Suzuki" where id =3;

-- 実データの解析
-- Categoryテーブルから10件だけ取得
select * from Category limit 10;
-- Categoryテーブル内の件数を取得
select count(*) from Category;

-- ZIPDescriptionテーブルから全件取得
select * from ZIPDescription;
-- ZIPDescriptionテーブルからPlaceNameだけ取得
select PlaceName from ZIPDescription;
-- ZIPDescriptionテーブルからPlaceNameを重複行を削除して取得
select distinct PlaceName from PlaceName;
-- 重複を除いたPlaceNameの数を取得
select count(distinct PlaceName) from ZIPDescription;
-- ZIPDescriptionテーブルからaで終わるstateを抽出
select distinct state from ZIPDescription where state like 'a%';
-- ZIPDescriptionテーブルからaで始まるstateの数を抽出
select count(distinct state) from ZIPDescription where staet like '%a';

-- 同じフィールドタイプをもつものをまとめて数えるときにgroup byを使う
-- ordersテーブルでpaymenttypeごとにレコードを取得するとき
select PaymentType,count(*) from Orders group by PaymentType;
-- 複数の条件でgroup byしてみる
select Channel, PaymentType ,count(*) as count from Orders group by Channel, PaymentType limit 100;
-- ProductArea, CategotyでOrderDetailテーブルのレコードをまとめてその数の降順に出力
select ProductArea, Category, count(*) as count from OrderDetail group by ProductArea, Categoty order by count desc;

-- HH_IDが1の世帯についてordersテーブルのレコード数とdollarsの合計、平均を取得
select HH_ID, count(*), sum(Dollars), avg(Dollars) from Orders where HH_ID=1;
-- havingを利用した条件の設定
-- HH_IDが10以下の世帯に対してOrdersテーブルからDollarsの合計と平均を求め、Dollarsの合計が300以上の世帯を表示
select HH_ID, count(*), sum(Dollars), avg(Dollars) from Dollars where HH_ID >=10 group by HH_ID having sum(Dollars) >= 300;
-- HH_IDが10以下の世帯について世帯ごとにOrderDetailテーブルのレコード数、全レコードのQuantityのごうけい及びQuantityの平均をもとめ、Quantityの平均が1.2以上のものを表示
select HH_ID, count(*), sum(Quantity), avg(Quantity) from OrderDetail where HH_ID <= 10 group by HH_ID having avg(Quantity) >= 1.2;
-- HH_IDが9の世帯について、Quantityが最大のものとQuantityが最小のレコードを表示
select HH_ID, max(Quantity), min(Quantity) from Orders where HH_ID =9;

-- Householdテーブルのフィールド名はHH_ID,ZIPCode
-- ZIPDescriptionテーブルのフィールド名はZIPCode,PlaceName,State,StateAbb,Country,Latitude,Longitude
-- Ordersテーブルのフィールド名はHH_ID,CompanyID,OrderNum,OrderDate,Dollars,PaymentType,Channel
-- OrderDetailテーブルのフィールド名はHH_ID,CompanyID,OrderNum,OrderDate,ProductArea,Category,Dollars,Quantity,Channel

-- 各世帯が住んでいる州を取得するためにHouseholdテーブルとZIPDescriptionテーブルを結合させる必要がある
select t1.HH_ID, t1.ZIPCode, t2.State from Household as t1 inner join ZIPDescription as t2 on t1.ZIPCode = t2.ZIPCode;
-- HH_IDが1の世帯について、ZIPCode, OrderNum, ProductArea, Categoryを取得するためにHouseholdテーブル、Ordersテーブル、OrderDetailテーブルを内部結合する
select t1.HH_ID, t1.ZIPCode, t2.OrderNum, t3.ProductArea, t3.Category from Household as t1 inner join Orders as t2 on t1.HH_ID = t2.HH_ID inner join OrderDetail as t3 on t2.OrderNum = t3.OrderNum where t1.HH_ID = 1;

-- OrdersテーブルとCorporationテーブルをCompanyIDで結合する
select HH_ID, CorporationID from Orders as t1 inner join Corporation as t2 on t1.CompanyID = t2. CompanyID;
-- OrdersテーブルとCorporationテーブルをCompanyIDで結合し、HH_IDが10未満の世帯について世帯ごとにCorporationIDでまとめ、CorporationIDごとにを求める
select HH_ID, CorporationID, count(*) from Orders as t1 inner join Corporation as t2 on t1.CompanyID = t2.CompanyID where t1.HH_ID <10 group by HH_ID, CorporationID;

-- サブクエリ
-- select fromで指定するテーブルに別のselectの結果を利用
-- HH_IDが10未満の世帯の中でHH_IDごとのDollarsの平均が300以上の世帯におけるデータを取得
select * from (select HH_ID, count(*), sum(Dollars) as sum_d, avg(Dollars) from Orders where HH_ID <= 10 group by HH_ID) as t1 where t1.sum_d >= 300;
-- 上と同じ結果を出力するクエリ
select HH_ID, count(*), sum(Dollars) as sum_d, avg(Dollars) from Orders where HH_ID <=10 group by HH_ID having sum_d >=300;

-- ZIPDescriptionテーブルからstateの数を重複を削除して取得する
-- サブクエリを使うと
select count(*) from (select state from ZIPDescription group by state) as t1;
サブクエリを使わないクエリは
select count(distinct state) from ZIPDescription;

-- NYにある世帯数を取得
select count(*) from Household where ZIPCode in (select ZIPCode from ZIPDescription where stateAbb = "NY");

-- HH_IDが10以下の世帯について、OrdersテーブルのDollarsの平均が全体の世帯平均よりも大きい世帯を表示
select HH_ID, avg(Dollars) as avg_D, (select avg(Dollars) from Orders) as total_avg from Orders where HH_ID <= 10 group by HH_ID having avg_D >= (select avg(Dollars) from Orders);

-- case when:selectするフィールドで条件を指定する
-- Dollarsが100以上ならHigh、50以上100以下ならMedium、50未満ならlowというAmountLevelをつけて、HH_ID、OrderNum,OrderDate,Dollarsを取得し、OrderDateの昇順で並べる
select HH_ID, OrderNUm, OrderDate, Dollars case whern Dollars >= 100 then "High" when Dollars >=50 and Dollars < 100 then "Medium" when Dollars < 50 then "low" end AmountLevel from Orders order by OrderDate;
-- 上と同様の条件でラベルをつけて各ラベルのデータ数をカウントを出力
select HH_ID, OrderNum, OrderDate, Dollars case when Dollars >= 100 then 1 else 0 end as "High", case when Dollars < 100 and Dollars >=50 then 1 else 0 end as "Medium", case when Dollars < 50 then 1 else 0 end as "Low" from Orders Order by Orderdate;

-- 世帯別にChannel別購入数が知りたとき
-- HH_IDが3以下でHH_IDとChannelごとのHH_ID,Channel,データ数を取得し、HH_IDの昇順で並べるクエリ
select HH_ID, Channel, count(*) from Orders where HH_ID <=3 group by HH_ID, Channel order by HH_ID;
-- HH_IDが3以下の世帯においてHH_ID、ChannnelのC,I,Oのそれぞれの数をHH_IDごとに取得し、HH_IDの昇順で取得するクエリ
select HH_ID, sum(Channel='C'), sum(Channel='I'), sum(Channel='O') from Orders where HH_ID <=3 group by HH_ID;
-- HH_IDが10以下の世帯において、orderdateを2005年,2006年,2007年に分類しHH_IDごとにデータ数を取得するクエリ
select HH_ID, count(*), sum(Orderdate >= "20050101" and OrderDate <= "20051231") as "2005",sum(Orderdate >= "20060101" and Orderdate <= "20061231") as "2006", sum

-- 覚えておくと便利なコマンド
-- describe <テーブル名>:テーブルに関する情報の表示
describe Category;
レスポンス例
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| CategoryID  | varchar(3)  | No   | PRI |         |       |
| Description | varchar(20) | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+

show database()  :現在選択しているデータベースを表示
show tables  :現在選択しているデータベース内のテーブル名を表示
show processlist  :現在サーバで動作しているプロセス(クエリ)の表示
kill <ID>  :プロセスの強制終了









