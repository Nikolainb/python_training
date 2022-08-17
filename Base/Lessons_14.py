def printpython():
    print("Python")
printpython()

def sum (x, y):
    return x + y
s = sum(5, 7)
print(s)

def sub(x,y):
    return x-y
b = sub(10,4)
print((b))

def summaprint(x, y, r = False):
    s = sum(x, y)
    if r:
        return s
    else:
        print(s)
summaprint(25, 7)

def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s
print((bigsum(1,5,8,0,1)))

print('Анонимные функции')
lamdafunc = lambda x, y:print(x+y)
lamdafunc(5,6)
print((lambda x, y: x + y) (1, 4))

result = (lambda x, y: x + y) (1, 4)
print(result)

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n >max:
            max = n
    return max
print(getmax([1,4,6,78,76,45,34,23]))

#HW
#1) Создайте функцию, которая проверяет чётное число передано в параметре или нет. Она должна возвращать True или False.
#2) Создайте функцию, которая принимает список и возвращает максимальное значение из списка.
#3) Создайте функцию с переменным числом аргументов, внутри которой должно выводиться среднее арифметическое переданных чисел.
#Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое на их количество.

def num(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(num(7))

spisok= [4,3,5,213,43,123,44,234,34,]
def maxnum():
    return max(spisok)
print(maxnum())

def avnum(x,y,z,a,b):
    return int((x+y+z+a+b)/5)
print(avnum(3,4,5,6,19))
