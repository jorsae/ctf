encoded = """tm bcsv qolfp
f'dmvd xuhm exl tgak
hlrkiv sydg hxm
qiswzzwf qrf oqdueqe
dpae resd wndo
liva bu vgtokx sjzk
hmb rqch fqwbg
fmmft seront sntsdr pmsecq"""

def get_word(words):
    print('%s\n' % words)
    
    passphrase = ""
    line = words.split("\n")
    for index in range(2):
        for i in range(len(line)):
            w = line[i].split(' ')
            pos = 0 if index == 0 else len(w) - 1
            pos2 = 0 if index == 0 else len(w[pos]) - 1
            passphrase += w[pos][pos2]
        index += 1
    print(passphrase)

def cipher():
    start = ord('a')
    end = ord('z')

    pw = ""
    index = 25
    for c in encoded:
        i = ord(c) - start
        if i >= 0 and i <= end:
            i -= index
            if i < 0:
                i +=26
            elif i > 26:
                i -= 26
            pw += chr(i+start)
            if index < 0:
                index = 25
        else:
            pw += c
            if pw == "'":
                continue
            index -= 1
    return pw

password = cipher()
get_word(password)