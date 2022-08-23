class Point:
    x = 0
    y = 0

p1 = Point()
print(p1.x, ';', p1.y)
print(p1)
p1.x = 5
p1.y = 7
print(p1.x, ';', p1.y)

p2 = Point()
p2.z = 10
print(p2.x, ';', p2.z)


#HW
#Создайте класс прямоугольника со следующими свойства: координаты левого верхнего угла, ширина и высота.
#Создайте экземпляр этого класса.
#Измените значения его свойств и выведите их.

class Rectangle:
    left_x = 1
    left_y = 10
    width = 300
    height = 500

r1 = Rectangle()
print(r1.left_y, ';', r1.left_x, ';', r1.width, ';', r1.height)

r2 = Rectangle()
r2.left_x_1 = 5
r2.left_y_1 = 10
r2.height_1 = 800
r2.width_1 = 100
print(r2.left_y_1, ';', r2.left_x_1, ';', r2.width_1, ';', r2.height_1)