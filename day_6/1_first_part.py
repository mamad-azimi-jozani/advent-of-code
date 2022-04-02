from collections import deque

with open('input.txt') as f:
    f = f.readlines()
fish_list = f[0].split(',')
fish_list = list(map(int,fish_list))




def lanternfish(fish_list, take_day=1):
    while take_day <= 18:
        for i in range(len(fish_list)):
            fish_list[i] = fish_list[i] - 1
            if fish_list[i] == -1:
                fish_list[i] = 6
                fish_list.append(8)
        # if take_day == 1:
        print(fish_list)
        take_day += 1


# print(lanternfish([3,4,3,1,2]))

