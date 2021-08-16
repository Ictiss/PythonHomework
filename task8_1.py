class Date:

    def __init__(self,dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def extract(cls, dd_mm_yyyy):
        date = []
        for i in dd_mm_yyyy.split('-'):
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):
        if 1<= day <= 31 and 1<= month <=12 and 0 <= year <= 2021:
            return 'Введена верная дата'
        else: return 'Ошибка при введении даты'

    def __str__(self):
        return f'Введенная дата: {Date.extract(self.dd_mm_yyyy)}'

day = Date('14 - 8 - 2021')

print(day.valid(14, 8, 2021))
print(day.extract('14 - 8 - 2021'))
print(day.valid(14, 14, 2021))

