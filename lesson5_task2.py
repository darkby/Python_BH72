"""Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число"""

while input('Continue yes/no ') != 'no':
 first_count = int(input('Введите первое число '))
 operand = input('Введите желаемое математическое действие(+-*/ **(возведение в степень) ')
 second_count = int(input('Введите второе число '))
 if operand == '+':
  print(int(int(first_count) + second_count))
 elif operand == '-':
  print(int(first_count - second_count))
 elif operand == '*':
  print(int(first_count * second_count))
 elif operand == '/':
  print(int(first_count / second_count))
 elif operand == '**':
  print(int(first_count ** second_count))
 else:
  print('Error of type operand')

