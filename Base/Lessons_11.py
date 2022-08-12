import random # ДЛЯ генерации случайного числа


myset = set()
print(myset)
myset = {}
print((myset))

myset = set("Python")
print(myset)

myset = {'1', 2, 3, 1, '1'}
print((myset))

print(int(random.random()*10))

list = [int(random.random()*10) for i in range(0, 10)]
print(list)
myset = set(list)
print(myset)