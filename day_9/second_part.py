import numpy as np


with open('input.txt') as f:
    f = [i.strip() for i in f.readlines()]

zero = np.zeros((len(f), len(f[0])))


f = [list(map(int, i)) for i in f]

for i in range(len(f)):
    zero[i] = f[i]



def basin(x, y):
    global counter

    counter += 1
    zero[x][y] = -1
    neighbors = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
    ]
    for x, y in neighbors:
        if 0 < x < len(zero) or 0 < y < len(zero[0]):
            if x >= 0 and y >= 0:
                if x < 100 and y < 100:
                    # print(x, y)
                    if zero[x][y] != 9 and zero[x][y] != -1:
                        zero[x][y] = -1
                        basin(x, y)
    return counter

l = []
for i in range(100):
    for j in range(100):
        if zero[i][j] != 9:
            counter = 0
            l.append(basin(i, j))
            # zero = data

x = sorted(l, reverse=True)[:3]
z = 1
for i in x:
    z *= i
print(z)











