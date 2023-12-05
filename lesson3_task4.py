"""Пользователь вводит 3 числа, сказать сколько из них положительных
и сколько отрицательных"""

n1 = int(input('First count '))
n2 = int(input('Two count '))
n3 = int(input('Three count '))
count_plus = (n1 >= 0) + (n2 >= 0 ) + (n3 >= 0)
count_minus = (n1 < 0) + (n2 < 0) + (n3 < 0)
print('Количество положительных чисел',int(count_plus))
print('Количество отрицательных чисел',int(count_minus))
