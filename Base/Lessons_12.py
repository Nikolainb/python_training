mytuple = tuple() # функция tuple позволяет создать кортеж
print(mytuple)
mytuple = (1, '3', '5')
print(mytuple)

mytuple = tuple('Python')
print(mytuple)


#HW
# Попросите пользователя ввести произвольную строку.
#Создайте кортеж, состоящий из символов, введённой пользователем строки.
#3) Выведите кортеж, используя цикл for.

a = tuple(input("Введите произвольную строку:"))
print(a)
for b in a:
    print(b)