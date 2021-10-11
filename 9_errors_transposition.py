from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if len(self.matrix) == len(other.matrix) and\
                len(self.matrix[0]) == len(other.matrix[0]):
            ans = deepcopy(self.matrix)

            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    ans[i][j] += other.matrix[i][j]

        else:
            raise MatrixError(self, other)

        return Matrix(ans)

    def __mul__(self, num):
        ans = deepcopy(self.matrix)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                ans[i][j] *= num

        return Matrix(ans)

    __rmul__ = __mul__

    def transpose(self):
        ans = []

        for i in range(len(self.matrix[0])):
            inter_ans = []
            for j in range(len(self.matrix)):
                inter_ans.append(self.matrix[j][i])
            ans.append(inter_ans)

        self.matrix = ans
        return Matrix(ans)

    def transposed(self):
        ans = []

        for i in range(len(self.matrix[0])):
            inter_ans = []
            for j in range(len(self.matrix)):
                inter_ans.append(self.matrix[j][i])
            ans.append(inter_ans)

        return Matrix(ans)


exec(stdin.read())
