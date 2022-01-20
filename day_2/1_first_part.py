import re
from collections import defaultdict

with open('input.txt', 'r') as myfile:
    myfile = myfile.read().split()

# dict = {myfile[i] + '_' + f'{i}': myfile[i+1] for i in range(0, len(myfile), 2)}

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
print(sum_up)
down = final.get('down')
sum_down = sum(list(map(int, down)))
print(sum_down)
print(sum_forward*(sum_up-sum_down))



# another way ;)

dict = {myfile[i] + '_' + f'{i}': myfile[i+1] for i in range(0, len(myfile), 2)}
# print(dict)


fwdObje = re.compile(r'forward_\d+')
dwnObje = re.compile(r'down_\d+')
upObje = re.compile(r'up_\d+')
sum_frwd = [dict[i] for i in dict.keys() if fwdObje.match(i)]
sum_dwn = [dict[i] for i in dict.keys() if dwnObje.match(i)]
sum_Up = [dict[i] for i in dict.keys() if upObje.match(i)]
x = sum(list(map(int, sum_frwd)))
y = sum(list(map(int, sum_dwn)))
z = sum(list(map(int, sum_Up)))
print(x*(y-z))
