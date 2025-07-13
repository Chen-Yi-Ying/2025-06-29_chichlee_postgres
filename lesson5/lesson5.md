### 建立新資料表

```sql
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20),
	major VARCHAR(20),
	PRIMARY KEY(student_id)
);
```

### 新增資料

```sql
INSERT INTO student VALUES(1,'小白','歷史');
INSERT INTO student VALUES(2,'小黑','生物');
DELETE FROM student WHERE student_id = '2';
INSERT INTO student VALUES(3,'小綠',NULL);
INSERT INTO student(student_id, name, major) VALUES(3,'小綠',NULL);
INSERT INTO student(name, major) VALUES('小綠',NULL);
```
