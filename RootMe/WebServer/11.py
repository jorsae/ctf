import requests

url = "http://challenge01.root-me.org/web-serveur/ch32/index.php"
r = requests.post(url, headers={'Referer':'http://challenge01.root-me.org/web-serveur/ch32/login.php'}, allow_redirects=False)
print(r.text)