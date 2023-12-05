"""Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
четные, потом нечётные"""

list_numeric = [101,101,22,3,4,45,6,77,7,8,88,88]
def random1(text):
    x = len(text)
    y = len(text)
    z = len(text)
    for i in text:
        x -= 1
        if i%2 == 0:
            text.append((i))
        if x == 0:
            break
    for i in text:
        y -= 1
        if i%2 != 0:
            text.append((i))
        if y == 0:
            break
    del text[0:z]
    print(text)
random1(list_numeric)