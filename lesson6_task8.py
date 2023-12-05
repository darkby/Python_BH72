"""Дан словарь, ключ - Название страны, значение - список городов, на вход
поступает город, необходимо сказать из какой он страны"""

terra = {'blr': ['minsk', 'gomel', 'brest'], 'rus': ['moskow', 'piter', 'kazan'], 'pl': ['warshava', 'bila-podlyaska', 'byalystok']}
print(terra)
def find_country(text):
    for i, j in terra.items():
        if text in j:
            print('Country it`s ', i)

find_country(input('Enter city please '))
