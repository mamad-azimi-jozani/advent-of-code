import numpy as np
with open('input.txt') as f:
    f = [i.strip() for i in f.readlines()]

# print(f)
zero = np.zeros((len(f), len(f[0])))

f = [list(map(int, i)) for i in f]

for i in range(len(f)):
    zero[i] = f[i]


adjacent = []
for i in range(len(f)):
    for j in range(len(f[0])):
        # top_left
        if i == 0 and j == 0:
            if zero[i][j] < zero[i+1][j] and zero[i][j] < zero[i][j+1]:
                adjacent.append(zero[i][j])
        # down_left
        if i == len(f)-1 and j == 0:
            if zero[i][j] < zero[i-1][j] and zero[i][j] < zero[i][j+1]:
                adjacent.append(zero[i][j])        # top_right
        if i == 0 and j == len(f[0])-1:
            if zero[i][j] < zero[i+1][j] and zero[i][j] < zero[i][j-1]:
                adjacent.append(zero[i][j])        # down_right
        if i == len(f)-1 and j == len(f[0])-1:
            if zero[i][j] < zero[i-1][j] and zero[i][j] < zero[i][j-1]:
                adjacent.append(zero[i][j])
        # corner_column_left without last and first
        if 1 <= i <= len(f)-2 and j == 0:
            if zero[i][j] < zero[i-1][j] and zero[i][j] < zero[i+1][j]:
               if zero[i][j] < zero[i][j+1]:
                   adjacent.append(zero[i][j])
        # corner_column_right without last and first
        if 1 <= i <= len(f)-2 and j == len(f[0])-1:
            if zero[i][j] < zero[i-1][j] and zero[i][j] < zero[i+1][j]:
               if zero[i][j] < zero[i][j-1]:
                   adjacent.append(zero[i][j])

        # top_row without last and first
        if i == 0 and 1 <= j <= len(f[0])-2:
            if zero[i][j] < zero[i][j-1] and zero[i][j] < zero[i][j+1] and zero[i][j] < zero[i+1][j]:
                adjacent.append(zero[i][j])
        #down_row without last and first
        if i == len(f)-1 and 1 <= j <= len(f[0])-2:
            if zero[i][j] < zero[i][j-1] and zero[i][j] < zero[i][j+1]:
               if zero[i][j] < zero[i-1][j]:
                   adjacent.append(zero[i][j])

        # other
        if 1 <= i <= len(f)-2 and 1 <= j <= len(f[0])-2:
            if zero[i][j] < zero[i][j-1] and zero[i][j] < zero[i][j+1]:
               if zero[i][j] < zero[i-1][j] and zero[i][j] < zero[i+1][j]:
                   adjacent.append(zero[i][j])

print(sum(adjacent)+len(adjacent))









































