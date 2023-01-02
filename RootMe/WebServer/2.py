import hashlib

print(hashlib.md5('https://reddit.com'.encode()).hexdigest())
# b59c8f81f47d204cec223000c847a0b4
"""
?url=https://reddit.com&h=b59c8f81f47d204cec223000c847a0b4
Flag: e6f8a530811d5a479812d7b82fc1a5c5

"""