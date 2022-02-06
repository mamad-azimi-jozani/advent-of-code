import numpy as np
import re

with open('input.txt') as my_file:
    my_file = my_file.readlines()

my_file = [i.strip() for i in my_file]
my_file = [re.sub(r'->', '', i) for i in my_file]
my_file = [re.sub('  ', ',', i) for i in my_file if i != '']
my_file = [re.sub(",", ' ', i) for i in my_file]
my_file = [i.split() for i in my_file]

x = []
for i in range(len(my_file)):
    for j in range(4):
        x.append(int(my_file[i][j]))
# print(x)


def convert_to_tuple(lst):
    x0 = lst[0]
    y0 = lst[1]
    x1 = lst[2]
    y1 = lst[3]
    if x0 == x1 or y0 == y1:
        left = [x0]+[y0]
        right = [x1]+[y1]
        return [left, right]
    else:
        return 0

final = []
for i in range(500):
    final.append(convert_to_tuple(x[4*i:4*i+4]))

final = list(filter(lambda x: x != 0 , final))
# print(final)
def test(lst1, lst2):
    x0 = lst1[0]
    y0 = lst1[1]
    x1 = lst2[0]
    y1 = lst2[1]
    if x0 == x1:
        if y1-y0 > 0:
            return [[x0, i] for i in range(y0, y1+1)]
        else:
            return [[x0, i] for i in range(y1, y0+1)]
    if y0 == y1:
        if x1-x0 > 0:
            return [[i, y0] for i in range(x0, x1+1)]
        else:
            return [[i, y0] for i in range(x1, x0+1)]


# print(test([0, 9], [5, 9]))
# print(test([7, 0], [7, 4]))
ff = []
for i in range(len(final)):
    ff.append(test(final[i][0], final[i][1]))
# print(ff)
fff = []
for i in range(len(ff)):
    for j in range(len(ff[i])):
        fff.append(ff[i][j])
fff = sorted(fff)
# print(fff)
fff = list(map(tuple, fff))
# print(fff)
count_item = {i: fff.count(i) for i in fff}
# print(count_item)
count_item = list(filter(lambda x: x if x >= 2 else 0, count_item.values()))
print(len(count_item))







