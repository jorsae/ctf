"""
96719db60d8e3f498c98d94155e1296aac105ck4923290c89eeeb3ba26d3eef92
65 chars long | sha2 = 64chars long
k = non-hex

96719db60d8e3f498c98d94155e1296aac105c4923290c89eeeb3ba26d3eef92
crackstation.net -> 4dM1n
"""
import hashlib
print(len('96719db60d8e3f498c98d94155e1296aac105ck4923290c89eeeb3ba26d3eef92'))
print(hashlib.sha1('4dM1n'.encode()).hexdigest())