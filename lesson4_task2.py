"""Без использования collections, написать программу, которая будет
создавать словарь для подсчитывания количества вхождений каждой
буквы в текст введенный с клавиатуры"""

text1 = input('Text please ')
uniq_symbols = {i: text1.count(i) for i in text1}
print(uniq_symbols)
