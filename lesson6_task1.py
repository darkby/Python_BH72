"""Написать функцию перевода десятичного числа в двоичное и обратно, без
использования функции int"""


def binary(decimal):
    print(bin(decimal))
    bin_code = bin(decimal)
    code_red = ''
    for i in range(2, len(bin_code)):
        code_red += bin_code[i]
    result = 0
    kk = 0
    for i in reversed(code_red):
        i = int(i)
        result += i * (2 ** kk)
        kk += 1
    print(result)

binary(decimal = int(input('Enter ')))
