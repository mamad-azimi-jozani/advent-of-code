from first_day import SyntaxScore
with open('input.txt') as f:
    f = [i.strip() for i in f.readlines()]


class Complete(SyntaxScore):
    key = {
        '<': '>',
        '[': ']',
        '{': '}',
        '(': ')',
    }
    def calculate(self):
        incomplete = []
        for j in self.data:
            counter = 0
            for i in j:
                if i in self.open:
                    self.stack.append(i)
                if i in self.close:
                    if self.stack[-1] + i in self.pair:
                        # print(stack[-1] + i)
                        self.stack.pop()
                    else:
                        self.illegal.append(i)
                        self.stack.pop()
                        counter += 1
                        break

            if counter == 0:
                incomplete.append(j)
        # print(incomplete)

        last = []
        for i in incomplete:
            para = []
            for j in i:
                if j in self.open:
                    para.append(j)
                    # print(j)
                if j in self.close:
                    # print(para)
                    if para[-1] + j in self.pair:
                        # print(para[-1] + j)
                        para.pop()

            last.append(list(map(lambda i: self.key[i], para))[::-1])
        # print(last)

        score = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4,
        }
        last_score = []
        for i in last:
            # print(i)
            total = 0
            for j in range(len(i)):
                total = 5 * total + score[i[j]]
            last_score.append(total)
        last_score = sorted(last_score)
        return last_score[len(last_score)//2]


x = Complete(f)
print(x.calculate())






