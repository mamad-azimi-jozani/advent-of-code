import numpy as np
import re
with open('input.txt') as my_file:
    my_file = my_file.readlines()


class Board:
    def __init__(self, data):
        self.data = data
        self.marked = np.zeros((5, 5))


    def check_marked(self, number):
        for i in range(5):
            for j in range(5):
                if self.data[i, j] == number:
                    self.marked[i, j] = 1

    def win(self):
        return self.marked.all(axis=0).any() or self.marked.all(axis=1).any()

    def score(self, called):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i, j] == 0:
                    score += self.data[i, j]
        return score*called










my_file = [i.strip() for i in my_file]

random_numbers = list(map(int, my_file[0].split(',')))
print(random_numbers)
boards = []
for i in range(100):
    new_board = np.zeros((5, 5))
    for j in range(5):
        this_line = my_file[i*6+j+2]
        this_row = re.sub(' +', ' ', this_line).strip().split(' ')
        # print(this_row)
        new_board[j] = [int(i) for i in this_row]
    boards.append(Board(new_board))

for r in random_numbers:
    for b in boards:
        b.check_marked(r)
        if b.win():
            print(b.score(r))
            exit()












