import numpy as np

from first import *


k = 0
while k >= 0:
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
    counter = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[0][0] == data[i][j]:
                counter += 1
                if counter == 100:
                    print(k+1)
                    k = -99999

    k += 1

print(data)