#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

while (quantity := int(input('Введите число сколько элементов должно отображаться: '))) < 1:
    print('Число должно быть целое и больше ноля!')

listOfSequence = list(map(lambda x: round((1+1/x)**x , 2), range(1, quantity+1)))
sum_ = sum(listOfSequence)
print(f'Последовательность из {quantity} чисел -{listOfSequence}')
print(f'Сумма всех элементов = {sum_}')