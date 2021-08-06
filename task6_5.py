class Stationery:
    title = 'Stationery'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    title = 'Ручка'
    def draw(self):
        return f'Вы взяли такй предмет как {self.title}! Начать  отрисовку ручкой.'

class Pencil(Stationery):
    title ='Карандаш'
    def draw(self):
        return f'{self.title}? Хороший выбор. Начать карандашную отрисовку.'


class Handle(Stationery):
    title = 'Маркер'
    def draw(self):
        return f'Хм-м-м. {self.title}? Если вы уверены, то запустим отрисовку маркером.'


pen = Pen()
print(pen.draw())

pencil = Pencil()
print(pencil.draw())

hand = Handle()
print(hand.draw())