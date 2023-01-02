"""with open('ch7.bin', 'rb') as f:
    p = f.read()
print(p)
-> L|k\x80y+*^\x7f*zo\x7f\x82*\x80kvsno|*k\x80om*vo*zk}}*cyvksr\x7f\x14\n
"""
a = 'L|k\x80y+*^\x7f*zo\x7f\x82*\x80kvsno|*k\x80om*vo*zk}}*cyvksr\x7f\x14\n'

for i in range(0, 26):
    pw = ''
    for c in a:
        pw += chr(ord(c) - i)
    print('%d: %s' % (i, pw))
