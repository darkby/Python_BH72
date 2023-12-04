# # #  Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)


terra = {'blr': ['minsk', 'gomel', 'brest'], 'rus': ['moskow', 'piter', 'kazan'], 'pl': ['warshava', 'bila-podlyaska', 'byalystok']}
print(terra)
def find_country(text):
    for i, j in terra.items():
        if text in j:
            print('Country it`s ', i)

find_country(input('Enter city please '))
