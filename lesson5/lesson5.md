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

### 如存在則刪除既有表格

```sql
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS branch CASCADE;
```

### 新建表格和主鍵

```sql
CREATE TABLE employee(
	emp_id SERIAL,
	name VARCHAR(20),
	birth_date DATE,
	sex VARCHAR(1),
	salary INT,
	branch_id INT,
	sup_id INT,
 	PRIMARY KEY(emp_id)
);
```

### 建foreign key

```sql
CREATE TABLE branch(
	 branch_id INT,
	 branch_name VARCHAR(20),
	 manager_id INT,
	 PRIMARY KEY(branch_id),
	 FOREIGN KEY(manager_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);
```

### 建foreign key

```sql
ALTER TABLE employee ADD FOREIGN KEY (branch_id)
REFERENCES branch(branch_id) ON DELETE SET NULL;

ALTER TABLE employee ADD FOREIGN KEY (sup_id)
REFERENCES employee(emp_id) ON DELETE SET NULL;
```
