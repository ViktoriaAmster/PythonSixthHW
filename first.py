#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('введите вещественное число: ')
sum_ = sum(map(int, filter(lambda x:(x != '.') and (x != ','), number)))
print(f'Сумма цифр в числе {number} = {sum_}')