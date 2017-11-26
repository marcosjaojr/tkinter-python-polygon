from math import *

class MatrixHelpers():

    def transpose_matrix(self, matrix):
        return list(zip(*matrix))

    def translate_vector(self, x, y, dx, dy):
        return x+dx, y+dy

    def matrix_multiply(self, matrix_a, matrix_b):
        zip_b = list(zip(*matrix_b))
        return [
            [sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b]
            for row_a in matrix_a]

    def rotate_along_x(self, x, shape):
        return self.matrix_multiply(
            [[1, 0, 0], [0, cos(x), -sin(x)], [0, sin(x), cos(x)]], shape)

    def rotate_along_y(self, y, shape):
        return self.matrix_multiply(
            [[cos(y), 0, sin(y)], [0, 1, 0], [-sin(y), 0, cos(y)]], shape)

    def rotate_along_z(self, z, shape):
        return self.matrix_multiply(
            [[cos(z), sin(z), 0], [-sin(z), cos(z), 0], [0, 0, 1]], shape)
