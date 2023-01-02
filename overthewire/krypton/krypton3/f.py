# WELL DONE THE LEVEL FOUR PASSWORD IS BRUTE

file = ['found1', 'found2', 'found3']
a = []

content = ''
with open('data/merged', 'r') as f:
	content += f.read()
"""
KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS



E T A O I N S H R D L U c m
S => 456 | E 100%
Q => 340 | A
J => 301 | T 100%
U => 257 | S 100%
B => 246 | O
N => 240 | N, R?
C => 227 | I
G => 227 | N
D => 210 | H
Z => 132 |
V => 130 | L
Z => 132
W => 131 | D
M => 88
Y => 85
T => 75
X => 72
K => 69
E => 64
L => 60
A => 56
F => 28
I => 20 | V
O => 12
H => 4
R => 4


and tha ent ion tio for nde has nce edt tis oft sth men
JDS => 62 | THE
QGW => 27 | AND
SQN => 23 | EAR
DSN => 22 | HER
DCU => 19 | HIS
SNS => 19 | E_E
JSN => 16 | TER
CGE => 16 | IN_
JDQ => 15 | THA
CBG => 15 | ION
UDQ => 14 | SHA
SUY => 14 | ES_
JCB => 14 | TIO
BXJ => 13
YSQ => 13
QNS => 13
SWQ => 13
SWC => 13

"""
swap = {
	'S':'E',
	'Q':'A',
	'J':'T',
	'U':'S',
	'N':'R',
	'C':'I',
	'D':'H',
	'V':'L',
	'I':'V',
	'G':'N',
	'W':'D',
	'B':'O',
	'X':'F',
	'M':'U',
	'Z':'C',
	'Y':'P',
	'K':'W',
	'A':'B'
}
"""
swap = {
	'S':'E',
	'D':'H',
	'Q':'A',
	'F':'V',	
	'J':'T',
	'N':'R'
}
swap = {'J':'T',
	'D':'H',
	'S':'E',
	'Q':'A',
	'G':'N',
	'W':'D',
	'C':'I',
	'J':'G',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
}
"""

new_content = ''
for c in content:
	if c in swap:
		new_content += swap[c]
	else:
		if c == ' ' or c == '\n':
			new_content += c
		else:
			new_content += '*'
print(new_content)