"""
1.
n = input('Ведите ваше имя: ')
b = input('Ведите ваш пароль: ')
c = input('Введите ваш возраст: ')
d = input(f'Ваши данные для входа в аккаунт: имя - {n}, пароль - {b}, возраст - {c}')

2.
n = int(input('Введите время в секундах: '))
hours = round(n/3600, 1)
minutes = round(n/60, 1)
print(f'Время в формате ч:м:с - {hours} : {minutes} : {n}')

3.
n = int(input('Введите число n:'))
m = (n*2)
k = (n*3)
q = str(n)
z = str(m)
b = str(k)
d = (q + z + b)
print(f'n + nn + nnn = {d}')

4.
n = int(input('Введите выручку фирмы: '))
b = int(input('Введите издержки фирмы: '))
if n > b:
    print(f'Финансовый результат - прибыль. Ее величина: {n-b}')
else:
    print('Финансовый результат - убыль.')
k = round((n-b)/n, 1)
print(f'Рентабельность выручки = {k}')
l = int(input('Введите численность сотрудников фирмы: '))
j = round((n-b)/l, 1)
print(f'Прибыль фирмы в расчете на одного сотрудника = {j}')


2.
number = int(input('Введите трёхзначное число: '))
if number < 1000 and number > 99:
    firstn = number//100
    secondn = (number - 100*firstn)//10
    thirdn = number - 100*firstn - 10*secondn
    count = firstn + secondn + thirdn
    print(f'Сумма цифр данного трёхзначного числа = {count}')
else:
    print('Данное число не является трёхзначным.')

4.
s = int(input('Введите количество журавликов кратное 6: '))
if s%6 == 0:
    katya = s/1.5
    serezha = (s - katya)/2
    petya = (s - katya)/2
    print(f'Катя сделала {katya} журавликов, Петя сделал {petya} журавликов, Серёжа сделал {serezha} журавликов.')
else:
    print('Введённое число не кратно 6.')
"""
6.
n = input('Введите номер билета, состоящий из 6 цифр: ')
x = [int(a) for a in n]
if x[0] + x[1] + x[2] == x[3] + x[4] + x[5]:
    print('Ваш билет является счастливым!')
else:
    print('Ваш билет не является счастливым.')