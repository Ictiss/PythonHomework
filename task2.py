print('Задание 1')

my_list = [10, 'двенадцать', 12.23, [3, 1], True]
print('В списке приведены элементы таких типов данных, как:')
for i in my_list:
    print(type(i))

print('\n')



print('Задание 2') #Обмен соседних элементов в списке

element = input('Введите последовательность элементов через пробел:')
list_el = element.split()

for i in range(0, len(list_el)-1, 2):
    list_el[i], list_el[i+1] = list_el[i+1], list_el[i]
print(list_el)



print('\n')

print('Задание 3')
#версия list

print('Версия с использованием ТОЛЬКО  list')
year = [['зима', 1, 2, 12], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень',9, 10, 11]] #ввести первым элементом малентького списка - название сезона
num = int(input('Введите номер месяца в виде целого числа:'))

for season in range(len(year)):
    if num in year[season]:
        print('указанный вами месяц относится к сезону: {0}'.format(year[season][0]))

print('\n')

#версия dict
print('Версия с использованием ТОЛЬКО dict')
month = {1 : 'winter', 2 : 'winter', 3 : 'spring', 4 : 'spring', 5 : 'spring',
         6 : 'summer', 7 : 'summer', 8 : 'summer', 9 : 'autumn',
         10 : 'autumn', 11 : 'autumn', 12 : 'summer' }
user = int(input('Введите номер месяца в виде целого числа:'))


if month.get(user) == 'winter':
    print('Данный месяц относится к зиме')
elif month.get(user) == 'spring':
    print('Данный месяц относится к весне')
elif month.get(user) == 'summer':
    print('Данный месяц относится к лету')
else: print('Данный месяц относится к осени')

print('\n')

#версия list и dict
print('Версия с использованием и list, и dict')

seasons = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень' : [9, 10, 11]}
number = int(input('Введите номер месяца в виде целого числа:'))

for a in seasons.keys():
    if number in seasons.get(a):
        print('данный месяц относится ко времени года: {0}'.format(a))

print('\n')

print('Задание 4')

words = input('Введите несколько слов через пробел: ')
list_words = words.split()

for i in range(len(list_words)):
    if len(list_words[i]) > 10:
        print(i + 1, list_words[i][:10],'\n')
    else: print(i+1, list_words[i],'\n')

print('\n')

print('Задание 5')

my_list = [8, 6, 3, 2, 2, 1]
numb = int(input('Введите новый элемент: '))
for i in range(len(my_list)):
    if numb == my_list[i]:
        my_list.insert(i + 1, numb)
        break
    elif numb > my_list[0]:
        my_list.insert(0, numb)
        break
    elif numb < my_list[-1]:
        my_list.append(numb)
        break
    elif numb < my_list[i] and numb > my_list[i+1]:
        my_list.insert(i + 1, numb)
        break
print('Пользователь ввел число {}. Итоговый рейтинг: {}'.format(numb, my_list))

print('\n')

print('Задание 6')
struct = []
check = input('Начать ввод? y/n: ')
while check == 'y':
    goods = dict({'название': input('Введите название товара: '), 'цена': int(input('Введите цену товара: ')),
             'количество': int(input('Введите количество товара: ')), 'eд': input('Введите единицу измерения: ')})
    struct.append((len(struct) + 1, goods))
    check = input('Продолжить ввод? y/n: ')

analytics = {}

for i in struct: #все еще не ясно
    str_num, str_dict = i
    for key, value in str_dict.items():
        list_v = analytics.get(key, [])
        if value not in list_v:
            list_v.append(value)
        analytics[key] = list_v
print('Анализ товара: ', analytics)







