print('Задание 1')

def divi(x,y) :
    if y == 0 or x == 0:
        print('Нельзя делить на 0')
        return None
    else: return x/y

x = int(input('Введите делимое: '))
y = int(input('Введите делитель: '))
print(divi(x, y))



print('\n')

print('Задание 2')

def profile(**args):
    return f" Имя: {args['name']}, Фамилия: {args['last_name']}, Дата рождения: {args['birthday'] }, " \
           f" Город проживания: {args['city'] }, email: {args['email'] },  Номер телефона: {args['phone'] }"

print(profile(name = 'Полина', last_name = 'Карпушова',  birthday = '19.09.1997',
              city = 'Москва', email = 'drogonre@gmail.com', phone = '89998887766'))

print('\n')

print('Задание 3')

#вариант без списка
def my_func1(x, y, z):
    if x >= y and z >= y:
        return x+z
    if x >= y and y >= z:
        return x + y
    if x < y and x < z:
        return y+z

x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))
print(my_func1(x, y, z))

# на чтобы перебрать все варианты верно, уходит слишком много строк кода!
# поэтому проще использовать списки и сортировку

def my_func2(x, y, z):
     list = sorted([x, y, z])
     return sum(list[1:])

x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))
print(my_func2(x, y, z))

print('\n')


print('Задание 4')

def my_func3(x,y):
    return x**y
x = int(input('действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func3(x,y))

#Вариант с использованием цикла довольно объемный и неудобный

def my_func4(x,y):
    i = 0
    a = 1   #для возведения в степень 0
    while i != abs(y):
        a = a*x
        i += 1
    b = 1/a
    return b

x = int(input('действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func4(x, y))




print('\n')

print('Задание 5')

def my_sum(sum):
    x = input('Введите числа, для выхода символ %: ')
    Continue = True
    list = x.split(' ')
    for i in list:
        if i == '%' :
            Continue = False
            break
        sum += int(i)
    print("current sum: {}".format(sum))
    return Continue, sum

Continue = True
sum = 0
while Continue == True:
    Continue, sum = my_sum(sum)

print("насуммировали на {}".format(sum))

print('\n')

print('Задание 6')
def int_func(x):
    list = x.split(' ')
    i = 0
    str = ''
    for i in range(len(list)):

       str += list[i].title() + ' '
    return str
x = input('Введите слово или несколько: ')
print(int_func(x))

# эм, вышло так, что у меня сразу получилась функция,
# которая может и одно словно вывести с заглавной буквы, и всю строку :'D


