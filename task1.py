print('Задание 1')


fruit = input('Какой Ваш любимый фрукт? ')
print('Ваш любимый фрукт ', fruit,'? Вау, мой тоже!')

num = int(input('А сколько штук Вы можете съесть? '))
print('Целых', num, '? Ого, как много!')

print('\n')

print('Задание 2')
time = int(input('Введите время в секундах: '))
hour = time//3600
min = (time%3600)//60
sec = (time%3600)%60

print("Ваше время: {0}:{1}:{2}".format(hour, min, sec))

print('\n')

print('Задание 3')

n = int(input('Введите число меньше 9: '))
print('Резултат: ', n + n*11 +n*111)

print('\n')


print('Задание 4')

num = input('Введите число: ') # Из-за возникающей далее ошибки вводим число не как int, а как строку
i = 0
numln = len(num) #узнаем длинну введеной строки.
max = 0

while i < numln:
    index_num = int(num[i]) #присваиваем промежуточному результату индекс, для дальнейшего сравнения?

    #можно ли использовать if?
    #можно
    if index_num >= max:
        max = index_num
    i +=1

print('Наибольшая цифра в числе {0}: {1}'.format(num,max))

print('\n')

print('Задание 5')

gain = int(input('Введите сумму выручки фирмы:'))
costs = int(input('Введите сумму издержек фирмы:'))

if gain > costs:
    print('Фирма работает в прибыль')
    profit = gain - costs
    print(f'Рентабельность выручки: {profit/gain * 100:.2f}%' )
    staff = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника: ', profit/staff)
elif gain < costs:
    print('Фирма работает в убыток')
else: print('У фирмы нулевая прибыль')

print('\n')

print('Задание 6')

start = int(input('Введите результат пробежки первого дня: '))
result = int(input('Введите желаемый результат: '))
i = 1

while start < result:
    start = (start * 0.1) + start
    i +=1

print('Вы достигнете не менее', result, 'километров на', i, '-й день занятий')




