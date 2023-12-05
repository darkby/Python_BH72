"""*Заполнить словарь где ключами будут выступать числа от 0 до n, а
значениями вложенный словарь с ключами "name" и "email", а значения
для этих ключей будут браться с клавиатуры"""

count = int(input('Enter count of pair name/email '))
test2 = {i: {'name': input(f'Enter name id {i} '), 'email': input(f'Enter email id {i} ')} for i in range(0, count)}
print(test2)