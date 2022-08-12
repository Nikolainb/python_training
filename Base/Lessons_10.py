array = [1, 5, 0, -5, 2.5]
for n in array:
    print(n)

str = "Python"
for s in str:
    print(s)

print("----------")
for s in str:
    if s == "Y":
        break
else:
    print("Символа Y  в строке ", str, "нет")

print("----------")
array = list(range(2, 15))# функция лист преобразует выражение в список, функция range выведет значения из указанного диапазона
print(array)
for n in array:
    print(n)

print("----------")

array = [ i for i in range(1, 10)]
print(array)
array = [ i * 2 for i in range(1, 10)]
print(array)