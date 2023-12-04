# first task (first way)
# n1 = (input('Text Please '))
# n2 = n1.split(' ')
# print('-'.join(n2))
# first task (two way)
# n1 = (input('Text Please '))
# n2 = (n1.count(' '))
# print(n1.replace(' ','-', n2))
# Second task
# n1 = int(input('Enter first number '))
# n2 = int(input('Enter two number '))
# n3 = int(input('Enter tree number '))
# print(round((n1+n2+n3)/3, 3))
# Three task
# name = (input('Enter Name '))
# age = (input('Enter Age '))
# city = (input('Enter City '))
# print('My name %s. I am %s years old. I am from %s'  % (name.capitalize(), age, city.capitalize()))
# print('My name {name2}. I am {age2} years old. I am from {city2}' .format(name2=name.capitalize(), age2=age, city2=city.capitalize()))
# print(f'My name {name.capitalize()}. I am {age} years old. I am from {city.capitalize()}')
# Four task
# n1 = int(input('First count '))
# n2 = int(input('Two count '))
# n3 = int(input('Three count '))
# b1 = (n1 >= 0) + (n2 >= 0 ) + (n3 >= 0)
# b2 = (n1 < 0) + (n2 < 0) + (n3 < 0)
# print('Количество положительных чисел',int(b1))
# print('Количество отрицательных чисел',int(b2))
# import callback


# First task (fisrt way)

# n1 = int(input('Enter decimal please '))
# a2 = [2] * n1
# b2 = list(range(1, n1+1))
# print(a2)
# print(b2)
# result_list = list(map(pow, a2, b2))
# print(result_list)

# First task (two way)

# list2 = [2**n for n in range(1, int(input('Enter decimal please '))+1)]
# print([list2])

# Two task

# text1 = input('Text please ')
# uniq_symbols = {i: text1.count(i) for i in text1}
# print(uniq_symbols)

#Three task

# '''
# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
# '''
#
# count = int(input('Enter count of pair name/email '))
# test2 = {i: {'name': input('Enter name '), 'email': input('Enter email ')} for i in range(0, count)}
# print(test2)

#Three homeworks first task
# '''Вывести первые N чисел кратные M и больше K'''
#
# m = int(input('Введите число "кратности " '))
# k = int(input('Введите число отсчёта K '))
# n = int(input('Введите количество выводимыx чисел '))
#
# x = 0
# k += 1
# while x < n:
#     if k % m == 0:
#         print(k)
#         k += 1
#         x += 1
#     else: k += 1

# # '''Сделать калькулятор: у пользователя
# # спрашивается число, потом действие и второе
# # число'''
#
# while input('Continue yes/no ') == 'no':
#  first_count = input('Введите первое число ')
#  operand = input('Введите желаемое математическое действие(+-*/ **(возведение в степень) ')
#  second_count = int(input('Введите второе число '))
#  if operand == '+':
#   print(int(int(first_count) + second_count))
#  elif operand == '-':
#   print(int(first_count - second_count))
#  elif operand == '*':
#   print(int(first_count * second_count))
#  elif operand == '/':
#   print(int(first_count / second_count))
#  elif operand == '**':
#   print(int(first_count ** second_count))
#  else:
#   print('Error of type operand')

# # **Вывести четные числа от 2 до N по 5 в строку
# list1 = []
# n = int(input('Enter N '))
# for j in range(2, n+1):
#   if j % 2 == 0 :
#    list1.append(j)
# k = 0
# while k < len(list1):
#   print(list1[k:k+5])
#   k += 5

#Function

# # Написать функцию перевода десятичного числа в двоичное и обратно, без
# # использования функции int
#
# def binary(decimal):
#     print(bin(decimal))
#     bin_code = bin(decimal)
#     code_red = ''
#     for i in range(2, len(bin_code)):
#         code_red += bin_code[i]
#     result = 0
#     kk = 0
#     for i in reversed(code_red):
#         i = int(i)
#         result += i * (2 ** kk)
#         kk += 1
#     print(result)
# binary(decimal = int(input('Enter ')))

# # # Код Морзе для представления цифр и букв использует тире и точки. Напишите
# # функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# # (словари в помощь)
#
# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
# def text_in_morze(text):
#     result = []
#     text_in_lower = text.lower()
#     space_count = text_in_lower.count(' ')
#     text_final = text_in_lower.replace(' ','', space_count)
#     for i in text_final:
#         result += morze.get(i)
#     print(result)
#
# text_in_morze(text = input('Enter text for codind in Morze '))

# # #Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

# list_numeric = [1,2,3,4,5,6,7]
# def list_right(numeric, x):
#     if x > len(list_numeric):
#         x = x%len(list_numeric)
#     num3 = numeric[len(list_numeric)-x:len(list_numeric)] + numeric[0:len(list_numeric)-x]
#     print(num3)
# list_right(list_numeric, int(input('Enter X(integer please) ')))


#  Дан список содержащий в себе различные типы данных, отфильтровать таким
# # образом, чтобы остались только строки, использование дополнительного списка
# # незаконно
#
# list1 = ['12', 'asdfa', '15.666', 'True', 'None', '{a:66}', '[lida]', 2 , 15 , 1550.66]
# print(list1)
# def sorted_list(list_text):
#     counter = 1
#     while counter != 0:
#         counter = 0
#         for i in list1:
#             if isinstance(i, (float, int, list, dict, tuple)):
#                 list1.remove(i)
#                 counter += 1
#     print(sorted(list1))
#
# sorted_list(list1)

# #  Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
# #
# list_numeric = [1,2,3,4,5,6,7]
# def revers_list(text):
#     z = 0
#     y = 1
#     while z != len(list_numeric)//2:
#          list_numeric[z], list_numeric[len(list_numeric) - y] = list_numeric[len(list_numeric) - y], list_numeric[z]
#          z += 1
#          y += 1
#     print(list_numeric)
#
# revers_list(list_numeric)

# # #  Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# # четные, потом нечётные
# # #
# list_numeric = [101,101,22,3,4,45,6,77,7,8,88,88]
# def revers_list(text):
#     x = len(text)
#     y = len(text)
#     z = len(text)
#     for i in text:
#         x -= 1
#         if i%2 == 0:
#             text.append((i))
#         if x == 0:
#             break
#     for i in text:
#         y -= 1
#         if i%2 != 0:
#             text.append((i))
#         if y == 0:
#             break
#     del text[0:z]
#     print(text)
# revers_list(list_numeric)

# # #  Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
# # #
# list_numeric = [101,101,22,3,4,45,6,77,7,8,88,88]
# def list_summ(text):
#     result = []
#     j = 1
#     result.append(text[1] + text[len(text) - 1])
#     text.append(text[0])
#     while j != (len(text) - 1):
#         result.append(text[j - 1] + text[j + 1])
#         j += 1
#     print(result)
# list_summ(list_numeric)

# # #  Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны


# terra = {'blr': ['minsk', 'gomel', 'brest'], 'rus': ['moskow', 'piter', 'kazan'], 'pl': ['warshava', 'bila-podlyaska', 'byalystok']}
# print(terra)
# def find_country(text):
#     for i, j in terra.items():
#         if text in j:
#             print('Country it`s ', i)
#
# find_country(input('Enter city please '))
