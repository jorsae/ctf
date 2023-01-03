flag = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'
flag_split = [flag[i:i+2] for i in range(0, len(flag), 2)]

key = []

a1 = int('13', 16) ^ ord('H')
key.append(a1)

a2 = int('4a', 16) ^ ord('T')
key.append(a2)

a3 = int('f6', 16) ^ ord('B')
key.append(a3)

a4 = int('e1', 16) ^ ord('{')
key.append(a4)

index = 0
output = ''
for f in flag_split:
    xor = int(f, 16) ^ key[index % len(key)]
    index += 1
    output += chr(xor)

print(output)