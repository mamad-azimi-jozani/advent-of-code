import re
with open('input.txt') as f:
    f = [i.strip() for i in f.readlines()]
    f = [i for i in f if i != '']

print(f)
dic = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

# print(f)
regex_pattern = re.compile('[^\|]+$')

list = []
for i in f:
    list.append(regex_pattern.findall(i))
total = []
for i in range(len(list)):
    total.append(list[i][0].strip())

print(total)

last = []
for i in total:
    last.append(i.split())

print(last)

wtf = []
for i in range(len(last)):
    for j in range(4):
        wtf.append(len(last[i][j]))

print(wtf)
counter = 0
for i in wtf:
    if i in dic.values():
        counter += 1

print(counter)

