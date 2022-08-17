isprint = True

def sum (x,y ):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s
x = input("Введите число 1")
y = input("Введите число 2")
print("Cумма равна ", sum(x, y))

def sub(x, y):
    global result4
    result = float(x) - float(y)

result = 0
sub(x,y)
print("Разность равна:", result)

#HW
#1) Создайте переменную со значением числа пи: «3.141592».
#2) Напишите функцию, которая будет возвращать площадь окружности по переданному в параметре радиусу.
#3) Проверьте работу функции.
#Примечание: площадь окружности = пи * радиус * радиус.
#Значение числа пи надо взять из глобальной переменной, созданной в первом пункте.

p = (3.141592)
print(p)
def plsh(p,r):
    m = (p * r * r)
    return m
print(plsh(p,4))