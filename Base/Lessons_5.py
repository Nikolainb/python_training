#Логические операции
b1 = True
b2= False
print("b1 =", b1)
print("b2 =", b2)
print("b1 or b2", b1 or b2) # логическое или если есть тру и фолс , то выведит тру
print("b1 and b2", b1 and b2) # логическое и , здесь вернет фолс, тру вернуло бы если бы было два тру
print("not b1", not b1) # отрицание, меняется на противоположное значение
print("b1 != b2", b1 != b2) # не равно
print("b1 == b2", b1 == b2) # проверка на равенство

x = 5
y = 7
print("x =", x)
print("y =", y)
print("x > y =", x > y)
print("x < y =", x < y)
print("x <= y =", x <= y)
print("x >= y =", x >= y)

a= True and (True or (False and True or False) and True or True != False)
print(a)