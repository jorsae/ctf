import requests

url = "http://challenge01.root-me.org/web-serveur/ch5/index.php"

r = requests.get(url, headers={'Header-RootMe-Admin':'1'})
print(r.text)