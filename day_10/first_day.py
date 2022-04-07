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



### oop ###
class SyntaxScore:
    def __init__(self, data):
        self.data = data

    # string = '{<[[]]>}<{[{[{[]{()[[[]'
    def calculate(self):
        stack = []
        close = ['>', ')', '}', ']']
        open = ['[', '<', '{', '(']
        pair = ['<>', '()', '{}', "[]"]
        illegal = []
        score = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
        }
        for j in self.data:
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

        return sum(list(map(lambda i: score[i], illegal)))
