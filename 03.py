# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, 
# которую необходимо посчитать.Вводится список чисел. Все числа списка находятся 
# на разных строках.
import random
lenght_list = random.randint(10, 100)
print(lenght_list)
list = [random.randint(0, 9) for _ in range(lenght_list)]
print(list)
list.sort()
print(list)
word = ''

my_dict = {}                                                    # решение задачи через список
for i in list:
    my_dict[i] = my_dict.get(i, 0) + 1
print(my_dict)

for item, count in my_dict.items():
  if (count // 2) == 1:
    word = 'пару'
  elif 1 < (count // 2) < 5:
    word = 'пары'
  else:
    word = 'пар'
  print (f"Число {item} имеет {count // 2} {word} в списке")



# for i in range(0, len(list)):                                                    # решение через цикл
#   count = 0
#   for j in range(len(list)):
#     if list[i] == list[j]:
#       count += 1
#   if (count // 2) == 1:
#     word = 'пару'
#   elif 1 < (count // 2) < 5:
#     word = 'пары'
#   else:
#     word = 'пар'
#   if list[i - 1] != list[i]:
#     print (f"Число {list[i]} имеет {count // 2} {word} в списке")

      