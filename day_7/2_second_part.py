import math
from numpy import median
with open('input.txt') as f:
    f = f.readlines()

fuels = list(map(int, f[0].split(',')))

def sum_number(number):
    return (number*(number+1))//2

# fuels = [16,1,2,0,4,2,7,1,2,14]
# print(sum(fuels)/len(fuels))



avg = math.floor(sum(fuels) / len(fuels))
# min_list = []
# fuel_spend = 0
# for i in range(min(fuels), max(fuels)+1):
#     for j in fuels:
#         fuel_spend += sum_number(abs(i-j))
#     min_list.append(fuel_spend)
#     fuel_spend = 0
# #
# # print(min(min_list))

xx = sum([sum_number(abs(avg-i)) for i in fuels])
print(xx)