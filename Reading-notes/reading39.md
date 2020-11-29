# SQLi with Burp Suite, WebGoat

[Link](https://www.varonis.com/blog/sql-injection-identification-and-prevention-part-1/)

- SQL stands for standardized query language. It is method of inserting, filtering, and retrieving information from a database. 
- With vulnerable Sql data, adversaries can exploit flaws in your web application - extracting user data.
- It is fairy common that sysadmin is paired to setup and administer sql server with little or no practical knowledge of how to actually craft queries.
- query = command
- SQLite is smallest database youll find in everyday use.
- At its core, a table is simply a list of information
- How to create and update dat with SQL commands

```sql
-- To insert into the existing table with the values
INSERT INTO
"your-table-name"
(column_name_1, column_name_2)
VALUES
(value_for_column_name_1, value_for_column_name_2)

-- To update product 
UPDATE 
Products
SET 
column_name_2 = new_value
WHERE 
Column_name_1 = some_value

-- To read data 
SELECT
(column_name_1, column_name_2)
FROM
your-table-name

-- To delete data
DELETE FROM
your-table-name
WHERE 
column-name_1 = your_value
```
`WHERE` is a command that you can run to give condition clause
- String conctenation for sql command can cause huge backlash.


```sql
-- Example of malicious sql commands
SELECT * FROM products WHERE id =
    (UPDATE products
     SET price = 0.1
     WHERE ID = 1)
```
- Frameworks help to prevent Sql injection
1. defeat common sql injection patterns by implementing line break, null character, single quotes, etc.

```ruby
# With Rails, this is the difference between:

# SQL String Concatention BAD
Model.where(“id = “ + id)
#And

# Parametized Query Good
Model.where(“id = ?”, id)

```

[ASP.net](https://msdn.microsoft.com/en-us/library/ff648339.aspx?f=255&MSPPError=-2147217396)


```
// for my own reference
# Database
- Sufficient and appropriate database user permissions set
- Extraneous or unused database features disabled
- Database logging enabled
-Database backup / restore procedure
- Database connection filtering procedures enabled (example: MySQL has options to prevent execution of multiple SQL - statements in a single query)
-Database drivers up to date
#Application
- Using filtering options
- Using parameterization options
- Using DB calls only when needed? (Could you use a static site generator?)
- Code lint/checks for potential SQL injection points
- Manual check for SQL Injection prone points
- Application logging
# Web Server / Web Firewall
- Use WAF SQL Injection pre-filters
- Rate limit to prevent mass SQL Injection attempts
- Alert on SQL Injection pattern attempts

```