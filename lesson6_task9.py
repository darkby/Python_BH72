"""Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
пустая строка)"""

terra = {'100': {'name' : 'alex', 'last_name': 'ivanov', 'phone' : '+375291234567', 'email': 'alex@mail.ru' },
         '101': {'name' : 'vova', 'last_name': 'sidoroff', 'phone' : '+375299876541',  },
         '102': {'name' : 'sofia', 'last_name': 'sergeeva', 'phone' : '+375296543217', 'email': '' }}

def email(dictionary):
    for i in dictionary:
        if dictionary[i].get('email') == None:
            print('Email отсутствует у ID', i, dictionary[i]['name'])
            print()
        if dictionary[i].get('email') == '':
            print('Email не указан у ID', i, dictionary[i]['name'])
            print()

email(terra)