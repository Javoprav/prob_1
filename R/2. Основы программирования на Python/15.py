def sum(x,y):     # локальные функции
 s =  float(x) + float(y)
 return s
x = input('Введите число - 1: ') # глобальные фунуции
y = input('Введите число - 2: ') # глобальные фунуции
print('Сумма равна: ', sum(x, y))

print("\n-----------------------\n")

isPrint = False
def sum(x,y):     
 s =  float(x) + float(y)
 if isPrint:
  print(s)
 else:
  return s
x = input('Введите число - 1: ') 
y = input('Введите число - 2: ') 
print('Сумма равна: ', sum(x, y))

result = 0
def sub (x, y):
 global result
 result = float(x) - float(y)
x = input('Введите число - 1: ') 
y = input('Введите число - 2: ') 
sub (x, y)
print('Разность равна = ', result)

'''1) Создайте переменную со значением числа пи: «3.141592».
2) Напишите функцию, которая будет возвращать площадь окружности по переданному в параметре радиусу.
3) Проверьте работу функции.
Примечание: площадь окружности = пи * радиус * радиус. Значение числа пи надо взять из глобальной переменной, созданной в первом пункте.'''

pi = 3.141592
def pl(r):
 global pi
 print (pi * r * r)
pl(8)