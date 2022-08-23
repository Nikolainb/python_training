
class Rectangle:
    left_x = 0
    left_y = 0
    width = 0
    height = 0
    def __init__(self, left_x=0, left_y=0, widnth=0, heigh=0):
        self.left_x = left_x
        self.left_y = left_y
        self.width = widnth
        self.height = heigh
    def __str__(self):
        return "Прямоуголник с координатами: (" + str(self.left_x) + ";" + str(self.left_y) + ") " + "Шириной:"+ str(self.width) +" и " + "Высотой:" + str(self.height)

    def range (self, r2):
        return self.width * self.height

    def range (self, r3):
        return (self.width + self.height) * 2

r1 = Rectangle(0, 0, 5, 2)
r2 = Rectangle(0,0,4,4)
r3 = Rectangle(0,0,5,1)
print(r1.left_x, ';', r1.left_y, ';', r1.width, ';', r1.height)
print(r1)
print(r2.range(Rectangle(0,0,4,4)))
print(r3.range(Rectangle(0,0,4,4)))
