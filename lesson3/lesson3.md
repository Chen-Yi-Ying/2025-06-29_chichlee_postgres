## 建立資料表的語法

```sql
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);
```

## 建立一個叫student的資料表

```sql
CREATE TABLE IF NOT EXISTS student (
   student_id SERIAL PRIMARY KEY,
   name VARCHAR(20) NOT NULL,
   major VARCHAR(20) UNIQUE
);
```

## 刪除資料表

```sql
DROP TABLE IF EXISTS student;
```

## 建立1筆資料
```sql
INSERT INTO student (name, major)
VALUES ('陳怡穎','企業管理');
```

## 建立多筆資料
```sql
INSERT INTO student (name, major)
VALUES ('小藍','英文'),('米奇','布魯托管理');
```

## 取得資料
```sql
SELECT student_id, name, major
FROM student;

SELECT *
FROM student
WHERE name = 'Winnie';

SELECT *
FROM student
ORDER BY student_id;

SELECT *
FROM student
ORDER BY student_id DESC;

SELECT *
FROM student
ORDER BY student_id DESC
LIMIT 2;
```
