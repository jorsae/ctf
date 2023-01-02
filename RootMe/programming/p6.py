"""
Password:
lFablYE9P1
"""

import requests
import re

cookie = {'PHPSESSID':'sessionId'}

r = requests.get('http://challenge01.root-me.org/programmation/ch1/', cookies=cookie)
html = r.text

num1 = re.search('= \[ (-)?\d+', html).group()
if '-' in num1:
    num1 = int(re.search('\d+', num1).group()) * -1
else:
    num1 = int(re.search('\d+', num1).group())
delimeter = re.search('\] \S \[', html).group()[2:-2]
num2 = int(re.search('n \* (-)?\d+ ]', html).group()[4:-2])
U0 = int(re.search('U\<sub\>0\<\/sub\> \= (-)?\d+', html).group()[16:])
iterations = int(re.search('\d{5,6}', html).group())

print('num1: %d' % num1)
print('Delimeter: %s' % delimeter)
print('num2: %d' % num2)
print('U0: %d' % U0)
print('Iterations: %d' % iterations)

"""
Formula is:
[ num1 + Un ] (+ or -) [ n * num2 ]
"""
previousU = U0
for i in range(1, iterations + 1):
    if delimeter == '+':
        previousU = num1 + previousU + ((i - 1) * num2)
    else:
        previousU = (num1 + previousU) - ((i - 1) * num2)

result = previousU
res = 'http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=%s' % result
r = requests.get(res, cookies=cookie)
print('Result: %d' % result)
print(r.text)
