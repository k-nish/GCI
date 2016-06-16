-- order byはgroup byの後に適用される
-- HH_IDごとにDollarsの最小値を取りたい場合
-- 正しいクエリ
select HH_ID, min(Dollars) from Orders where HH_ID in (1,3) group by HH_ID order by Dollars limit 10;
Dollarsが最小値のレコードを抽出する場合
select HH_ID, min(Dollars) from Orders where HH_ID in (1,3) group by HH_ID;

-- 結合
-- HouseholdテーブルとZIPDescriptionテーブルでZIPCodeで連結してZIPCodeとStateをつなげるクエリ
select HH_ID, l.ZIPCode, r.State from Household as l inner join ZIPDescription as r on l.ZIPCode = r.ZIPCode where l.HH_ID <= 5;
-- 外部結合をしてZIPCodeとstateをつなげて取り出すクエリ
select l.ZIPCode, l.state from ZIPDescription as l left join Household as r on l.ZIPCode = r.ZIPCode where r.ZIPCode is NULL;
-- NULLかどうかを確認するためにはis NULLという条件が正しく、where r.ZIPCode = NULLとしても上のクエリは動かない。

インデックスの利用?

-- 遷移の抽出
select HH_ID OrderDate as current, (select min(OrderDate) from Orders as sub where sub.HH_ID = main.HH_ID and sub.OrderDate > main.OrderDate) as next from Orders as main where HH_ID=3 order by OrderDate;

MariaDB固有の関数
group_concat
select HH_ID, group_concat(distinct Channel order by Channel ) from Orders where HH_ID = 1;

-- with rollup  :group byしたときに値が入ってないものをまとめてnullとして表示する
select Channel, count(*) as count from Orders group by Channel with rollup;
-- レスポンス例
+---------+----------+
| Channel | count    |
+---------+----------+
| C       |  7338615 |
| I       |  4557623 |
| O       |  1263904 |
| NULL    | 13160142 |
+---------+----------+
