"""Вывести первые N чисел кратные M и больше K"""

multiplicity = int(input('Введите число "кратности " '))
start_number = int(input('Введите число отсчёта K '))
count = int(input('Введите количество выводимыx чисел '))

x = 0
start_number += 1
while x < count:
    if start_number % multiplicity == 0:
        print(start_number)
        start_number += 1
        x += 1
    else: start_number += 1
