# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во 
# втором массиве. Пользователь вводит число N - количество элементов 
# в первом массиве, затем N чисел - элементы массива. Затем число M - 
# количество элементов во втором массиве. Затем элементы второго массива
import random
lenght_list1 = random.randint(10, 15)
list_1 = [random.randint(0, 20) for _ in range(lenght_list1)]
print()
print(list_1)
print()
lenght_list2 = random.randint(10, 15)
list_2 = [random.randint(0, 20) for _ in range(lenght_list2)]
print(list_2)
list_3 = []

# for i in range(len(list_1)):
#   flag = True
#   for j in range(len(list_2)):
#     if list_1[i] == list_2[j]:
#       flag = False
#       break
#     else:
#       flag = True
#   if flag == True:
#     list_3.append(list_1[i])    


# for i in list_1:
#   if i not in list_2:
#     list_3.append(i)

list_3 = [i for i in list_1 if i not in list_2]

print()
print(list_3)
print()