"""Пользователь вводит Имя, Возраст и Город, сформировать
приветственное сообщение путем форматирования 3-мя способами"""

name = (input('Enter Name '))
age = (input('Enter Age '))
city = (input('Enter City '))
print('My name %s. I am %s years old. I am from %s'  % (name.capitalize(), age, city.capitalize()))
print('My name {name2}. I am {age2} years old. I am from {city2}' .format(name2=name.capitalize(), age2=age, city2=city.capitalize()))
print(f'My name {name.capitalize()}. I am {age} years old. I am from {city.capitalize()}')