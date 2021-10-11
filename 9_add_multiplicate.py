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

    def __add__(self, other):
        ans = deepcopy(self.matrix)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                ans[i][j] += other.matrix[i][j]

        return Matrix(ans)

    def __mul__(self, num):
        ans = deepcopy(self.matrix)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                ans[i][j] *= num

        return Matrix(ans)

    __rmul__ = __mul__


exec(stdin.read())
