var data = unescape("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30");
var tab = data.split(',');
var password = "";
for(let i = 0; i < tab.length; i++){
    password += String.fromCharCode(tab[i]);
}
console.log(password); //786OsErtk12