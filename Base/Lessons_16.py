import math
import random

import calc
import mymodule


print(random.randint(0,10))
print(math.sin(1))

while True:
    print('1 -Сложение; 2 - Вычитание; 3- Умножение; 4- Деление; 0 -Выход' )
    code = input('Введите команду: ')
    if code == '0':
        exit(0)
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    if code =='1':
        r = calc.sum(a,b)
    elif code=='2':
        r = calc.sub(a,b)
    elif code =='3':
        r == calc.div(a,b)
    elif code == '4':
        r ==calc.mult(a,b)
    print("Результат: ", r)


#hw
#1) Создайте свой модуль и подключите его в основном файле.
# Напишите в модули 3 функции, каждая из которых принимает список.
# Первая функция – получение максимального значения, вторая – получение минимального значения, третья – получение суммы всех элементов.
#3) Проверьте работу этих функций в основном файле



spisok= [4,3,5,213,43,123,44,234,34,]
a = mymod
print(a)
