from numpy import median

with open('input.txt') as f:
    f = f.readlines()

fuels = list(map(int, f[0].split(',')))
# print(len(fuels))


# min_list = []
# fuel_spend = 0
# for i in fuels:
#     for j in fuels:
#         fuel_spend += abs(i-j)
#     min_list.append(fuel_spend)
#     fuel_spend = 0
#
# print(min(min_list))

### another way ###

median = median(fuels)

part_1 = sum([abs(median-i) for i in fuels])
print(part_1)
