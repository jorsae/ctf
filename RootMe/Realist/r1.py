import requests

s = requests.Session()
r = requests.Request("GETS", 'http://challenge01.root-me.org/realiste/ch3/admin/')

prepped = s.prepare_request(r)
resp = s.send(prepped)

print(resp.text)