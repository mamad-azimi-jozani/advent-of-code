import numpy as np

with open('test.txt') as f:
    f = [list(i.strip()) for i in f.readlines()]
# print(f)

for i in range(len(f)):
    f[i] = list(map(int, f[i]))

data = np.zeros((len(f), len(f[0])))

for i in range(len(f)):
    data[i] = f[i]

def test(x, y):

    if x-1 >= 0 and data[x-1][y] != -1:
        data[x-1][y] += 1
        if data[x-1][y] > 9:
            data[x-1][y] = -1
            test(x-1, y)

    if x+1 < len(data) and data[x+1][y] != -1:
        data[x+1][y] += 1
        if data[x+1][y] > 9:
            data[x+1][y] = -1
            test(x+1, y)

    if y+1 < len(data[0]) and data[x][y+1] != -1:
        data[x][y+1] += 1
        if data[x][y+1] > 9:
            data[x][y+1] = -1
            test(x, y+1)

    if y-1 >= 0 and data[x][y-1] != -1:
        data[x][y-1] += 1
        if data[x][y-1] > 9:
            data[x][y-1] = -1
            test(x, y-1)
    #
    if x+1 < len(data) and y+1 < len(data[0]):
        if data[x+1][y+1] != -1:
            data[x+1][y+1] += 1
            if data[x+1][y+1] > 9:
                data[x+1][y+1] = -1
                test(x+1, y+1)

    #
    if x+1 < len(data) and y-1 >= 0:
        if data[x+1][y-1] != -1:
            data[x+1][y-1] += 1
            if data[x+1][y-1] > 9:
                data[x+1][y-1] = -1
                test(x+1, y-1)
    #
    if x-1 >= 0 and y-1 >= 0:
        if data[x-1][y-1] != -1:
            data[x-1][y-1] += 1
            if data[x-1][y-1] > 9:
                data[x-1][y-1] = -1
                test(x-1, y-1)

    #
    if x-1 >= 0 and y+1 < len(data[0]):
        if data[x-1][y+1] != -1:
            data[x-1][y+1] += 1
            if data[x-1][y+1] > 9:
                data[x-1][y+1] = -1
                test(x-1, y+1)

# test(2, 2)
# counter = 0
if __name__ == '__main__':
    for k in range(95):
        for i in range(len(data)):
            for j in range(len(data)):

                if data[i][j] != -1:
                    data[i][j] += 1

                if data[i][j] > 9:
                    data[i][j] = -1
                    test(i, j)

        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] == -1:
                    data[i][j] = 0


    print(data)
    # print(counter)



