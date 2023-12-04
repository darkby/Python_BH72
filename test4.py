a1 = [1, 3, 5, 7, 9, 11, 13]
print('Length list: ', len(a1))
print('last element of list: ', a1[len(a1)-1])
kk = []
j = 1
kk.append(a1[1]+a1[len(a1)-1])
a1.append(a1[0])
while j != (len(a1)-1):
    kk.append(a1[j-1]+a1[j+1])
    j += 1
print(kk)

