import re
with open('input.txt') as f:
    f = [i.strip() for i in f.readlines()]
    f = [i.split("|") for i in f]
    f = [(i.split(), j.split()) for i, j in f]

# print(f)

def intersect(a, b):
    return len(set(a).intersection(b))

def change_to_number(parameter1: list, parameter2: list):


    seven_dict = {
        1 : sorted(list(filter(lambda i: i if len(i) == 2 else 0, parameter1))[0]),
        4 : sorted(list(filter(lambda i: i if len(i) == 4 else 0, parameter1))[0]),
        7 : sorted(list(filter(lambda i: i if len(i) == 3 else 0, parameter1))[0]),
        8 : sorted(list(filter(lambda i: i if len(i) == 7 else 0, parameter1))[0]),
    }

    for i in parameter1:
        # this is for 0,6,9
        if len(i) == 6:
            if intersect(i, seven_dict[4]) == 4:
                seven_dict[9] = sorted(i)

            if intersect(i, seven_dict[7]) == 3 and intersect(i, seven_dict[4]) == 3:
                seven_dict[0] = sorted(i)

            if intersect(i, seven_dict[7]) == 2:
                seven_dict[6] = sorted(i)

        # this for 2,3,5
        if len(i) == 5:
            if intersect(i, seven_dict[1]) == 2:
                seven_dict[3] = sorted(i)

            if intersect(i, seven_dict[4]) == 2:
                seven_dict[2] = sorted(i)

            if intersect(i, seven_dict[1]) == 1 and intersect(i, seven_dict[4]) == 3:
                seven_dict[5] = sorted(i)

    # print(seven_dict)
    value = [sorted(x) for x in parameter2]
    # print(value)
    total_value = ''
    for i in value:
        for k,v in seven_dict.items():
            if i == v:
                total_value += str(k)

    return int(total_value)

#
tt = []
for i in range(len(f)):
    tt.append(change_to_number(f[i][0], f[i][1]))
print(sum(tt))































