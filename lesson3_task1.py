"""Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
способами"""

text = (input('Text Please '))
text2 = text.split(' ')
print('-'.join(text2))
text2 = (text.count(' '))
print(text.replace(' ','-', text2))
