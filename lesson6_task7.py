"""Дан список чисел, необходимо для каждого элемента посчитать сумму его
соседей, для крайних чисел одним из соседей является число с противоположной
стороны списка"""

list_numeric = [101,101,22,3,4,45,6,77,7,8,88,88]
def list_summ(text):
    result = []
    j = 1
    result.append(text[1] + text[len(text) - 1])
    text.append(text[0])
    while j != (len(text) - 1):
        result.append(text[j - 1] + text[j + 1])
        j += 1
    print(result)
list_summ(list_numeric)

