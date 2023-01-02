data = 'OMQEMDUEQMEK'

start = ord('A')
end = ord('Z')

for i in range(26):
    output = ''
    for c in data:
        num = ord(c)
        num += i
        if num > end:
            num += start - end - 1
        output += chr(num)
    print(f'[{i}] {output}')

# rot14 = CAESARISEASY