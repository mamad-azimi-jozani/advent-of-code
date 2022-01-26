from math import pow
with open('input.txt') as my_file:
    my_file = my_file.read().split()



test = ['00100', '11110', '10110','10111','10101','01111','00111','11100','10000','11001','00010','01010',]

# , , '', '110010000101', '000111001111'
# print(test[1][1])
counter_0 = 0
counter_1 = 0
d = []
for i in range(12):
    for j in range(len(my_file)):
        # print(test[j][i])
        if int(my_file[j][i]) == 0:
            counter_0 += 1
        if int(my_file[j][i]) == 1:
            counter_1 += 1

    print('0:', counter_0)
    print('1:', counter_1)
    if counter_0 > counter_1:
        d.append(0)
    else:
        d.append(1)
    counter_0 = 0
    counter_1 = 0
    # print('///////')
print(d)

x = [1,0,1]
y = []
for i in range(12):
    y.append(int(pow(2,i)))
# print(x)
y = y[::-1]
binary = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
z = 0

x = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0]
b = [1 if b == 0 else 0 for b in x]
for i in range(len(x)):
    z += b[i]*binary[i]
print(z)
# print(b)
# print(1616*2479)

