""" Doesn't work """
"""
Kan ikke være Basic realm greiene
ER det på andre challenges også
"""

import requests

url = "http://challenge01.root-me.org/web-serveur/ch8/"

r = requests.get(url, headers={'WWW-Authenticate':'Basic realm="My Realm"'})
print(r.text)