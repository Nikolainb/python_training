# Сделайте у класса из предыдущего упражнения закрытыми все его поля.
# Добавьте методы get и set для всех полей. Поскольку полей всего 4, то должно быть 4 метода get и 4 метода set.
# Убедитесь, что доступа к полям уже нет за пределами класса.
# Проверьте работу методов get и set.
# Сделайте закрытый метод printlog(), в котором с помощью функции print() выводите значение переданного параметра.
#В методах get и set вызывайте метод printlog с параметром: «Запрошено свойство NAME» (для методов get)
# или «Изменено свойство NAME» (для методов set). Вместо NAME должно быть подставлено имя соответствующего свойства.

class Rectangle:
    __x = 0
    __y = 0
    __w = 0
    __z = 0
    def __init__(self, x, y, w, z):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__z = z

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getW(self):
        return self.__w
    def getZ(self):
        return self.__z

    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setW(self, w):
        self.w = w
    def setZ(self,z):
        self.z = z



p = Rectangle(0)
# print(p.__left_x)
p.setX(20)
print(p.setX())
print(p.getZ())
