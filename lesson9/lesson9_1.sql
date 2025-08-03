select count(*) as "筆數"
from "台鐵車站資訊";

select count(name) as "台北車站數"
from "台鐵車站資訊"
where "stationAddrTw" like '%臺北%';

select count(*)
from "每日各站進出站人數" left join "台鐵車站資訊"
on "車站代碼" = "stationCode"
where "stationName" = '基隆'

/*
 * 全省各站點2022年進站總人數-自己的版本
 */

select "stationName" as 站名, sum("進站人數") as 總人數
from "每日各站進出站人數" left join "台鐵車站資訊"
on "車站代碼" = "stationCode"
where "日期" between to_date('2022/01/01','YYYY/MM/DD') and to_date('2022/12/31','YYYY/MM/DD')
group by "stationName"

/*
 * 全省各站點2022年進站總人數-老師的版本
 */

SELECT "name" AS 站名,COUNT("name") AS 筆數,AVG("進站人數") AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name"

SELECT "name" AS 站名,date_part('year',"日期") AS "年份",COUNT("name") AS 筆數,AVG("進站人數") AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name","年份"

SELECT "name" AS 站名,date_part('year',"日期") AS "年份",COUNT("name") AS 筆數,AVG("進站人數") AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "name" = '基隆'
GROUP BY "name","年份"
ORDER BY "進站人數" DESC;

/*
 * 全省各站點2022年進站總人數大於5佰萬人的站點
 */

SELECT
    t."stationName" AS "車站名稱",
    SUM(p."進站人數") AS "2022年進站總人數"
FROM "每日各站進出站人數" p
LEFT JOIN "台鐵車站資訊" t ON p."車站代碼" = t."stationCode"
WHERE DATE_PART('year', p."日期") = 2022
GROUP BY t."stationCode", t."stationName"
HAVING SUM(p."進站人數") > 5000000
ORDER BY SUM(p."進站人數") DESC;


/*
*基隆火車站2020,2021,2022,每年進站人數
*/

SELECT
    date_part('year', p."日期") AS "年份",
    SUM(p."進站人數") AS "進站人數"
FROM "每日各站進出站人數" p
LEFT JOIN "台鐵車站資訊" t ON p."車站代碼" = t."stationCode"
WHERE t."stationName" = '基隆'
  AND date_part('year', p."日期") IN (2020, 2021, 2022)
GROUP BY date_part('year', p."日期")
ORDER BY "年份";

| 年份  | 進站人數  |
|-------|-----------|
| 2020  | 2,540,259 |
| 2021  | 2,058,217 |
| 2022  | 2,253,504 |

/*
*基隆火車站,臺北火車站2020,2021,2022,每年進站人數
*/

SELECT
    date_part('year', p."日期") AS "年份",
    SUM(CASE WHEN t."stationName" = '基隆' THEN p."進站人數" ELSE 0 END) AS "基隆進站人數",
    SUM(CASE WHEN t."stationName" = '臺北' THEN p."進站人數" ELSE 0 END) AS "臺北進站人數"
FROM "每日各站進出站人數" p
LEFT JOIN "台鐵車站資訊" t ON p."車站代碼" = t."stationCode"
WHERE t."stationName" IN ('基隆', '臺北')
  AND date_part('year', p."日期") IN (2020, 2021, 2022)
GROUP BY date_part('year', p."日期")
ORDER BY "年份";

| 年份  | 基隆進站人數 | 臺北進站人數 |
|-------|--------------|--------------|
| 2020  | 2,540,259    | 19,448,681   |
| 2021  | 2,058,217    | 14,488,139   |
| 2022  | 2,253,504    | 16,565,031   |

/*
*查詢 2022 年平均每日進站人數超過 2 萬人的站點
*/

SELECT
    t."stationName" AS "車站名稱",
    ROUND(AVG(p."進站人數"), 2) AS "平均每日進站人數"
FROM "每日各站進出站人數" p
LEFT JOIN "台鐵車站資訊" t ON p."車站代碼" = t."stationCode"
WHERE DATE_PART('year', p."日期") = 2022
GROUP BY t."stationName"
HAVING AVG(p."進站人數") > 20000
ORDER BY "平均每日進站人數" DESC;

| 車站名稱 | 平均每日進站人數 |
|----------|------------------|
| 臺北     | 45383.65         |
| 桃園     | 20680.88         |