# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
# определит количество элементов, у которых два соседних и, при этом, оба соседних 
# элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

import random
lenght_list = random.randint(6, 99)
list = [random.randint(0, 20) for _ in range(lenght_list)]
print(list)
count = 0
for i in range(len(list) - 1):
  if i == 0:
    if list[len(list) - 1] < list[i] > list[i + 1]:
      count += 1
  elif i == len(list):
    if list [i - 1] < list[i] > list[0] and list[i]:
      count += 1
  else:
    if list[i + 1] < list[i] > list[i - 1]:
      count += 1
print(count)