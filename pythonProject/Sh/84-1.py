'''18. Напишите программу, которая определяет, является ли вве-
денное натуральное число палиндромом.
Палиндром — число, буквосочетание, слово или текст,
одинаково читающееся в обоих направлениях.'''

n1 = input("Введите число: ")
n2 = n1[::-1]
if n1 == n2:
 print('Палиндром', n2)
else:
    print ('нихуа')

"""19. Напишите программу, находящую наибольший общий дели-
тель (НОД) двух целых положительных чисел a и b, вводимых
с клавиатуры."""

