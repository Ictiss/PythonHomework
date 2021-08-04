print('Задание 1')
file = open('text1.txt', 'w')
text = input('Введите данные? Для окончания ввода данных пустая строка:  ')
while text:
    file.write(text + '\n')
    text = input('Введите данные? Для окончания ввода данных пустая строка: ')


file.close()

print('\n')

print('Задание 2')
with open('text1.txt', 'r') as file2:
    cont = file2.readlines()            #Очень долго программа делила мне наполнение файлы на слова, считая их за строки, Ошибка - вместо readlines было readline
    print('Количество строк: ', len(cont))
    for i in range(0, len(cont)):
        print(len(cont[i].split(' ')))
        print('Количество слов в ', i+1, '-й строке - ', len(cont[i].split()))

print('Задание 3')
with open('text3.txt', 'r') as file3:
    str = file3.readlines()
    #str = l = [line.rstrip() for line in str] # При чтении из файла в конце каждой строки выводилось \n и все приводило к ошибке
    #Ошибка была не в этом, поэтому эта строчка не нужна
    print(str)
    sum = 0
    for i in str:
        last_name, salary = i.split(' ')
        sum += int(salary)
        if int(salary) < 20000:
             print(f'Зарплата {last_name} меньше 20000. Его зарплата составляет: {salary}')
    average = sum/len(str)
    average = float('{:.3f}'.format(average))
    print('Средняя зарплата сотрудников: ', average)

print('задание 4')
num ={'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре' }
new_w = []
with open('text4.txt', 'r') as file4:
    #with open('text4_2.txt', 'w')
    for i in file4:
        i = i.split(' - ')
        print(i)
        new_w.append(num[i[0]] + ' - ' + i[1])
        print(new_w)
with open('text4new.txt', 'w') as file4new:
    file4new.writelines(new_w)


print('задание 5')
with open('text5.txt', 'w') as file5:
    numb = input('Введите числа через пробел: ')
    file5.writelines(numb)
    num = numb.split(' ')
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)

print('задание 6')
sub = {}
with open('text6.txt', 'r') as file6:
    for i in file6:
        name, *lessons = i.split()
        lesson = [int(el.rstrip('(l)(pr)(lab)'))  for el in lessons if el != '-']
        sub[name.rstrip(':')] = sum((lesson))
print(sub)

print('задание 7')
import json
result = []
profit = {}
loss = {}
with open('text7.txt', 'r') as file7:
    average = []
    for el in file7.readlines():
        name, _, rev, costs = el.rstrip().split()
        prof = int(rev) - int(costs)
        if prof > 0:
            average.append(prof)
            profit.update({name: prof})
        else:
            loss.update({name: prof})
    result.append(profit)
    result.append(loss)
    result.append({'average_prof': sum(average)/len(average)})

with open('text7.json', 'w') as file7:
    json.dump(result, file7)
