mydict = dict() # функция  dict позволяет нам создавать словарь
print(mydict)

mydict = {"Name": 'John',"Age ": '35'}
print(mydict)

mydict = dict (Name='John', Age=35, isMale=True)
print(mydict)

print((mydict['Age']))
print("-----------")

for key in mydict:
    print(key, '=', mydict[key])

mytuple = ('Name', 'Age', 'isMale')
for key in mytuple:
    print(key, '=', mydict[key])

print("-----------")

mydict = {str(i * 2) : i for i in range(1, 10)}
print(mydict)

#HW
#1) Создайте словарь с двумя ключами «Name» и «Age» и значениями «Без имени» и «-1».
#2) Попросите пользователя ввести своё имя.
#3) Попросите пользователя ввести свой возраст.
#4) Примите эти данные и измените соответствующие элементы словаря.
#5) Выведите этот словарь (ключи и значения), используя цикл for.

mydict = dict(Name = 'Без имени',Age = -1)
name= input('Введите свое имя:')
age= int(input('Введите свой возраст'))
mydict['Name']=name
mydict['Age']=age
print(mydict)
for item in mydict.items():
    print(item)