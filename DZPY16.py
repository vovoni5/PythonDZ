'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''

n = int(input('Введите колличество чисел: '))

myList = []

for i in range(n):
    myList.append(i + 1)

print(myList)

k = int(input('Введите загадонное число: '))
count = 0

for i in range(len(myList)):
    if myList[i] == k:
        count += 1
print(count)