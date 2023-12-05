"""Дан список чисел, необходимо его развернуть без использования метода revese и
функции reversed, а так же дополнительного списка и среза"""

list_numeric = [1,2,3,4,5,6,7]
def revers_list(text):
    z = 0
    y = 1
    while z != len(text)//2:
         text[z], text[len(text) - y] = text[len(text) - y], text[z]
         z += 1
         y += 1
    print(text)

revers_list(list_numeric)
