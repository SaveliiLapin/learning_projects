from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        end_str = []

        for i in range(len(self.matrix)):
            end_str.append('\t'.join(map(str, self.matrix[i])))

        return '\n'.join(end_str)

    def size(self):
        return len(self.matrix), len(self.matrix[0])


exec(stdin.read())
