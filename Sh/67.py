"""11. Напишите программу, которая просит пользователя ввести
целое число. Далее:
• если число оказалось отрицательным, то выводит предыдущее число;
• если число оказалось положительным, то выводит следующее число;
• в любом другом случае программа выводит «0»."""

x = (float(input('ввести целое число: ')))
if x < 0:
    print('предыдущее число')
elif x > 0:
    print('следующее число')
else:
    print(0)