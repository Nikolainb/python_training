age  = 24  #integer - число
print("Vozrast:"+ str(age)) # функция str преобразовывает численное значение переменной age в строковое
print("Vozrast:", age) # из-за заяптой преобразовывать не нужно

temp = 5.6 #float -дробное число
print("Temperatura:", temp, "gradusov")

username = "Alex" # string строки
print("Imya polzovatelya:", username)

isexists = True # boolean
print("Существует", isexists)
isexists = False # boolean
print("Существует", isexists)

ten = "14.5"
print("Возраст:", ten)

print("Тип переменной:", type(ten)) # функция type позволяет определить тип переменной

#HW
#Создайте переменную со значением 10.
ages = 10
#Выведите данную переменную с помощью функции print().
print(ages)
#Измените значение переменной на 15.
ages = 15
#Выведите значение переменной в таком виде: «Значение переменной ИМЯ_ПЕРЕМЕННОЙ равно ЗНАЧЕНИЕ_ПЕРЕМЕННОЙ»
print("Значение перемнной ages равно ", ages)
#Создайте 2 строковые переменные со значениями: «Значение переменной» и «равно».
cda = "Значение переменной"
dda = "Равно"
#Выведите аналогичную строку из пункта 4, но с использованием переменных из пункта 5.
print(cda,dda,ages)
#Создайте 2 булевских переменных со значениями: True и False.
bbb = True
ccc = False
# Выведите их так, как написано в 6 пункте (то есть с использованием строковых переменных).
print(cda, dda, bbb)
print(cda, dda, ccc)
