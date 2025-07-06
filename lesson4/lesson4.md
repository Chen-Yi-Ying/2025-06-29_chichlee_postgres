## 更改日期型態和更新字串為DATE

```sql
ALTER TABLE world
ALTER COLUMN 日期 TYPE DATE
USING 日期::DATE; 
```
