class Circle:
    x = 0
    y = 0
    r = 0
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

c = Circle(5, 7, 10)
print(c.x, ';', c.y, ';', c.r)


#HW
# Возьмите за основу класс прямоугольника из предыдущего упражнения.
# Создайте у него конструктор, принимающий в качестве параметров все его свойства.
# Внутри конструктора инициализируйте свойства переданными в него параметрами.
# Используя конструктор, создайте экземпляр класса.
# Выведите его свойства.

class Rectangle:
    left_x = 0
    left_y = 0
    width = 0
    height = 0
    def __init__(self, left_x, left_y, widnth, heigh):
        self.left_x = left_x
        self.left_y = left_y
        self.width = widnth
        self.height = heigh


r1 = Rectangle(10, 4, 3, 54)
print(r1.left_x, ';', r1.left_y, ';', r1.width, ';', r1.height)

