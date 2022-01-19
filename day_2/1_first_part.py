import re
from collections import defaultdict

with open('input.txt', 'r') as myfile:
    myfile = myfile.read().split()

# dic = {myfile[i] + '_' + f'{i}': myfile[i+1] for i in range(0, len(myfile), 2)}

keys = [myfile[i] for i in range(0, len(myfile), 2)]
values = [myfile[i] for i in range(1, len(myfile), 2)]
dic = defaultdict(list)
for key, value in zip(keys, values):
    dic[key].append(value)

final = dict(dic)

forward = final.get('forward')
sum_forward = sum(list(map(int, forward)))
print(sum_forward)
up = final.get('up')
sum_up = sum(list(map(int, up)))
down = final.get('down')
sum_down = sum(list(map(int, down)))
print(sum_forward*(sum_up-sum_down))

