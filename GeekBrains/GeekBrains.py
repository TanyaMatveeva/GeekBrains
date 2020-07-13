# original_password = 'x777'
# password = input('Введите пароль: ')
# access = False
# if password == original_password:
#     print('пароль принят, добро пожаловать в систему')
#     access = True
#     if password != original_password:
#         print('Пароль неверен, вход запрещен')
# # Урок 1. Задание 1.
p1 = 'Посчитаем '
p2 = 'суммы'
print(p1 + p2)
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
summ_numbers = number1 + number2
print('Сумма чисел', number1, 'и', number2, 'равна', summ_numbers)

# # Урок 1. Задание 2.
time_second = int(input('Введите количество секунд: '))
min1 = time_second//60
hour = min1//60
min = min1 - (hour*60)
sec = time_second - ((min + (hour*60))*60)
print(f'{hour}:{min}:{sec}')

# Урок 1. Задание 3.
n = input('Введите число n: ')
nn = n + n
n_input = int(n)
nnn = nn + n
nn_input = int(nn)
nnn_input = int(nnn)
summ = int(n_input + nn_input + nnn_input)
print(f'{n}+{nn}+{nnn}={summ}')

# Урок 1. Задание 4.
# array =


# Урок 1. Задание 5.
#
revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if revenue <= costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в прибыль')
    user = int(input('Введите кол-во сотрудников для расчета рентабельности: '))
    profit = (revenue - costs) / user
    print('Прибыль фирмы на одного сотрудника составила', profit)

# Урок 1. Задание 6.

a = int(input('Результат спортсмена в перый день: '))
b = int(input('Желаемый результат в км: '))
i = 1
while a <= b:
    i += 1
    a = a + (a * 0.1)

print(f'на {i} день спортсмен достигнет результата - не менее {b} км')
