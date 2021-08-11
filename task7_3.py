class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        if self.quantity < 0 :
             print('Количество ячеек должно быть положительным!')


    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity < 0:
            print('Отрицательное число! действие невозможно')
            return None
        else:
            return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, cell_num):
        return (('*' * cell_num) + '\n') * (self.quantity // cell_num) + '*' * (self.quantity % cell_num)
cell1 = Cell(12)
cell2 = Cell(15)


print(cell1.make_order(5))
print(cell2.make_order(5))