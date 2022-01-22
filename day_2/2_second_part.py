import re
import itertools
with open('input.txt') as myfile:
    myfile = myfile.read().split()

my_dict = {myfile[i] + "_" + f'{i}': int(myfile[i+1]) for i in range(0, len(myfile), 2)}
fwd_obj = re.compile(r'forward_\d')
up_obj = re.compile(r'up_\d')
down_obj = re.compile(r'down_\d')
fwd_horizantol = sum([my_dict[i] for i in my_dict.keys() if fwd_obj.match(i)])
d = []
horizontal = 0
aim = 0
depth = 0
for key, value in my_dict.items():
    if up_obj.match(key):
        depth -= value
    if down_obj.match(key):
        depth += value
    if fwd_obj.match(key):
        horizontal = value
        aim += horizontal * depth
        print(aim)

print(aim*fwd_horizantol)



