"""Дан список чисел и на вход поступает число N, необходимо сместить список на
указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]"""

list_numeric = [1,2,3,4,5,6,7]
def list_right(numeric, x):
    if x > len(numeric):
        x = x % len(numeric)
    num3 = numeric[len(numeric)-x:len(numeric)] + numeric[0:len(numeric)-x]
    print(num3)
list_right(list_numeric, int(input('Enter X(integer please) ')))