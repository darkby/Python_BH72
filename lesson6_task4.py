"""Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы остались только строки, использование дополнительного списка
незаконно"""

list1 = ['12', 'asdfa', '15.666', 'True', 'None', '{a:66}', '[lida]', 2 , 15 , 1550.66]
print(list1)
def sorted_list(list_text):
    counter = 1
    while counter != 0:
        counter = 0
        for i in list1:
            if isinstance(i, (float, int, list, dict, tuple)):
                list_text.remove(i)
                counter += 1
    print(sorted(list_text))

sorted_list(list1)