class Shape:
    x = 0
    y = 0
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print('(' + self.x + ';' + self.y + ')')
    def draw(self):
        print("Рисуем фигуру")

class Circle(Shape):
    r = 0
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r
    def draw(self):
        print("Рисуем окружность (", self.x, ';', self.y, ';', self.r, ')')

class Rectangle(Shape):
    w = 0
    h = 0
    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
    def draw(self):
        print("Рисуем прямоугольник (", self.x, ';', self.y, ';', self.w, ';', self.h, ')')
s = Shape(5, 7)
s.draw()

c = Circle(10,4,5)
c.draw()

r = Rectangle(12,4,5,8)
r.draw()
