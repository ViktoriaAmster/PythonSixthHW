# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

ourList = [1, 7, 7, 7, 6, 9, 3, 1, 2, 4, 9]
print(list(filter(lambda x: ourList.count(x) == 1, ourList)))