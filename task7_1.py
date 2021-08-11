class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        strr = '\n'
        for line in self.matr:
            for i in line:
                strr += f'{i:>4}'
            strr += '\n'
        return  strr

    def __add__(self, other):
        list = []
        if len(self.matr) != len(other.matr):
            print('Проверьте размер складываемых матриц')
            return None
        for i in range(len(self.matr)):
            if len(self.matr[i]) != len(other.matr[i]):
                print('Проверьте размер складываемых матриц')
                return None

            line = []
            for k in range(len(self.matr[i])):
                line.append(self.matr[i][k] + other.matr[i][k])
            list.append(line)

        return Matrix(list)

matr1 = Matrix([[1, 2, 3], [5, 4, 7], [9, 8, 6]])
matr2 = Matrix([[5, 4, 9], [3, 7, 8], [1, 2, 6]])
print(f'matr1 = {matr1}')
print(f'matr2 = {matr2}')
print(f'matr1+matr2 = {matr1 + matr2}')