import numpy as np
with open('1_Sonar-Sweep.txt') as myfile:
    myfile = myfile.read()

myfile = myfile.split()
myfile = list(map(int,myfile))

y = {f'{i}': myfile[i:3+i] for i in range(0,len(myfile)-2)}

counter = 0
for i in range(len(y.keys())-1):
    if sum(list(y.values())[i]) < sum(list(y.values())[i+1]):
        counter += 1
print(counter)
