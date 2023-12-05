"""Пользователь вводит 3 числа, найти среднее арифметическое с
точность 3"""

n1 = int(input('Enter first number '))
n2 = int(input('Enter two number '))
n3 = int(input('Enter tree number '))
print(round((n1+n2+n3)/3, 3))
