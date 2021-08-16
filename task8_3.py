class Err:
    def __init__(self, *args):
        self.numbs = []

    def my_input(self):
        while True:
            try:
                num = int(input('Введите значения и нажимайте Enter: '))
                self.numbs.append(num)

            except:
                print("Недопустимое значение")
                exit = input('Попробовать еще раз? y/n ')

                if exit == 'Y' or exit == 'y':
                    print(self.my_input())
                elif exit == 'N' or exit == 'n':
                    return f'Ввод символов завершен. Результат ввода: {self.numbs}'
                else: return 'Экстренное завершение программы'



lix = Err()
print(lix.my_input())