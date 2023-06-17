'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X'''

n = int(input('Введите колличество чисел: '))

myList = []

for i in range(n):
    myList.append(i + 1)

print(myList)

k = int(input('Введите загадонное число: '))
number = 0
for i in range(len(myList)):
    min = k - myList[i]
    if min >= 0:
        number = myList[i]
    else:
        break
print(number)