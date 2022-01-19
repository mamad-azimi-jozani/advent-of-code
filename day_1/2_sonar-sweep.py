import numpy as np
with open('1_Sonar-Sweep.txt') as myfile:
    myfile = myfile.read()

myfile = myfile.split()
myfile = list(map(int,myfile))

myfile_dict = {f'{i}': myfile[i:3+i] for i in range(0,len(myfile)-2)}

counter = 0
for i in range(len(myfile_dict.keys())-1):
    if sum(list(myfile_dict.values())[i]) < sum(list(myfile_dict.values())[i+1]):
        counter += 1
print(counter)
