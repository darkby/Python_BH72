"""**Вывести четные числа от 2 до N по 5 в строку"""

list1 = []
n = int(input('Enter N '))
for j in range(2, n+1):
  if j % 2 == 0:
   list1.append(j)
k = 0
while k < len(list1):
  print(list1[k:k+5])
  k += 5
