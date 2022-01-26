# CO2 scrubber rating ---> the least common
# oxygen generator rating ---> the most common
with open('input.txt') as my_file:
    test = my_file.read().split()

# test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
def oxygen_generator_rating(number, position):
    if int(number[position]) == 1:
        return True
    else:
        return False

print(oxygen_generator_rating('00100',0))
counter_0 = 0
counter_1 = 0
position = 0
for i in range(12):
    for j in range(len(test)):
        if int(test[j][i]) == 0:
            counter_0 += 1
        elif int(test[j][i]) == 1:
            counter_1 += 1
    # print(counter_0)
    # print(counter_1)
    # print('//////')
    # print(test)
    if counter_1 > counter_0:
        test = [i for i in test if oxygen_generator_rating(i, position)]
        # print(test)
    if counter_0 > counter_1:
        test = [i for i in test if not oxygen_generator_rating(i, position)]
    if counter_0 == counter_1:
        test = [i for i in test if oxygen_generator_rating(i, position)]
    if len(test) == 1:
        break
    position += 1
    counter_0 = 0
    counter_1 = 0
print(test)
# counter_0 = 0
# counter_1 = 0
# position = 0
# for i in range(12):
#     for j in range(len(test)):
#         if int(test[j][i]) == 0:
#             counter_0 += 1
#         elif int(test[j][i]) == 1:
#             counter_1 += 1
#     # print(counter_0)
#     # print(counter_1)
#     # print('//////')
#     # print(test)
#     if counter_1 > counter_0:
#         test = [i for i in test if not oxygen_generator_rating(i, position)]
#         # print(test)
#     if counter_0 > counter_1:
#         test = [i for i in test if oxygen_generator_rating(i, position)]
#         # print(test)
#     if counter_0 == counter_1:
#         test = [i for i in test if not oxygen_generator_rating(i, position)]
#         # print(test)
#     if len(test) == 1:
#         break
#     position += 1
#     counter_0 = 0
#     counter_1 = 0
# print(test)

binary = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
x = ['111010000100']
y = ['011000111111']
x = list(map(lambda x: int(x), x[0]))
y = list(map(lambda y: int(y), y[0]))
print(x)
print(y)
z = 0
for i in range(len(y)):
    z += int(x[i])*binary[i]
print(z)
print(1599*3716)
# print(y[0][1])




