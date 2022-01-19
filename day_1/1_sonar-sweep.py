with open('1_Sonar-Sweep.txt') as myfile:
    myfile = myfile.read()

myfile = myfile.split()
depth_list = list(map(lambda x: int(x), myfile))

def test(number):
    x = []
    for i in range(0,len(number)-1):
        if number[i] < number[i+1]:
            x.append(number[i+1])
    return x


print(len(test(depth_list)))