i = 0   # создадим переменную i и присвоим ей значение 0
while i < 10:  # Пока переменная i меньше 10 , то будет выполняться условие
    i = i + 1
    print("Hello world")
print("Цикл завершен")

print("-----------")

i = 0
while i <10:
    i = i + 1
    if i == 5:# если i у нас в цикле равно 5 , значит у нас истина и команда continue переходит на следующий шаг
        continue
    if i == 8:  # если i у нас в цикле равно 8 , значит у нас истина и команда break завершает шаг
        break
    print(i)
print("Цикл завершен, i =", i)


print("-----------")

s = 0
x = 1
to = 10
while x <= to:
    s = s + x
    x = x + 1
print("Сумма чисел от 1 до", to, "равна", s)


while True:
    code = input("Введите 0 для выхода")
    if code == "0":
        break

print("-----------")
i = 1000
while True:
    i = i + 1
    print(i)



a = 1000
b = 0.1
while True:
    a = a * b
    print(int(a))

print("-----------")
i = 1000
while True:
    i = i + 1
    print(
        1i)
