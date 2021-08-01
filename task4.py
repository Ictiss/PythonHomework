'''print('Задание 1')

from sys import argv
script_name, a, b, c = argv
print('Отработка: {}, Ставка в час: {}, Премия: {}'.format(a, b, c))
print('Зарплата: ', int(a)*int(b) + int(c))

print('\n')'''

print('Задание 2')

list = [2, 34, 5, 3, 45, 1, 4, 3, 2, 1, 345, 64, 234, 74, 75, 76, 854]
new_list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1] ]
print('Первоначальный список чисел: ', list)
print('Результат: ', new_list)
print('\n')

print('Задание 3')
list = [i for i in range(20, 240) if i % 20 ==0 or i % 21 == 0]
print(list)
print('\n')

print('Задание 4')
list = [2,43,23, 54, 76, 265, 43, 675, 23, 5, 1, 2, 54, 675, 65, 87, 5 ]
new_list = [i for i in list if list.count(i) == 1]
print(f'Исходный: {list}')
print(f'Результат: {new_list}')
print('\n')

print('Задание 5')

from functools import reduce
list = [i for i in range(100, 1001) if i % 2 == 0]

print(f'Исходный список: {list}')

result =  reduce(lambda a,b: a*b, list)
print(result)
print('\n')

print('Задание 6. a')
from itertools import count, cycle
import sys
start = int(input('Введите число: '))
def generator(start):
    for i in count(start):
        if i > start + 15:
            break
        yield i

for i in generator(start):
    print(i)


print('Задание 6. б')
from random import randint
list = [randint(0, 5) for i in range(5)]
print(list)
a = 0
for i in cycle(list):
    if a > len(list)*2 - 1:
        break
    print(i)
    a += 1
print('\n')

print('Задание 7')

from itertools import count, cycle
from functools import reduce
def func(x,y):
    return x*y

def fact(n):
    for i in count(1):
        if i <= n:
            res = reduce(func, range(1, i+1))
            yield res
        else: break
n = int(input('Введите число: '))
for i in fact(n):
    print(i)

