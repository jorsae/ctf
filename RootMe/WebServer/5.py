import requests

url = "http://challenge01.root-me.org/web-serveur/ch2/"

r = requests.get(url, headers={'User-Agent':'admin'})
print(r.text)