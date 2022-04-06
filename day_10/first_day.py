with open('input.txt') as f:
    f = [i.strip() for i in f.readlines()]
# print(f)




string = '{<[[]]>}<{[{[{[]{()[[[]'
stack = []
close = ['>', ')', '}', ']']
open = ['[', '<', '{', '(']
pair = ['<>', '()', '{}', "[]"]
illegal = []
for j in f:
    for i in j:
        if i in open:
            stack.append(i)
        if i in close:
            if stack[-1] + i in pair:
                # print(stack[-1] + i)
                stack.pop()
            else:
                illegal.append(i)
                stack.pop()
score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

print(sum(list(map(lambda i: score[i], illegal))))