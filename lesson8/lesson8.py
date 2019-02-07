# """
#     Создайте класс Figure. У каждой фигуры есть имя, также можно найти площадь и периметр фигуры (методы square и perimeter).
#
#     Создайте классы Triangle, Circle, Rectangle производные от Figure.
#
#     У класса Triangle есть 3 стороны: a, b, c;
#     у Circle - радиус r;
#     у Rectangle - стороны a и b.
#
# Переопределите методы нахождения площади и периметра для каждой фигуры (Triangle, Circle, Rectangle).
#
# Также для объектов классов должны работать операторы сравнения: ==, >, < <=, >=.
#
#     Будем считать, что фигуры равны, если они имеют одинаковую площадь.
#
# Строковое представление объекта должно возвращать тип фигуры и её имя в следующем формате:
# например для Circle(name='abc', r=2) - Circle:"abc"
#
# Также необходимо обработать возможные исключения: r, a, b, c > 0, треугольник существует, если сумма любых двух сторон больше третьей.
# Инче должно быть выброшено соответствующее исключение, классы исключений определить самостоятельно.
# *Напишите декоратор, который будет кэшировать результаты вызова методов square и perimeter.
# Дополнительная функциональность приветствуется.
# """
# import functools
# from math import pi
#
#
# @functools.total_ordering
# class Figure:
#         def __init__(self, name="", a=0, b=0, c=0):
#             self.name = name
#             self.a = a
#             self.b = b
#             self.c = c
#
#         def square(self, a, b):
#             f = a*b
#             return f
#
#         def perimeter(self, a, b):
#             a = self.a
#             b = self.b
#             return a*2 + b*2
#
#         def __name__(self):
#             return self.name
#
#         def __str__(self):
#             return f'{self.__class__.__name__}:"{self.__name__}"'
#
#         def __eq__(self, other):
#             return self.square == other.square
#
#         def __lt__(self, other):
#             return self.square < other.square
#
#
# class Triangle(Figure):
#
#     def __init__(self, name="", a=0, b=0, c=0):
#         super().__init__()
#
#
#
#     def square(self, a, b, c):
#         s = (a+b+c)/2
#         p = s*(s-a)*(s-b)*(s-c)
#         f = p**0.5
#         return f
#
#     def perimeter(self, a=0, b=0, c=0):
#         return a+b+c
#
#
# class Circle(Figure):
#
#     def __init__(self, name="", r=0):
#         self.radius = r
#         self.name = name
#
#
#     def square(self, r):
#         return float((pi * r) ** 2)
#
#     def perimeter(self, r):
#         d = r*2
#         C = pi*d
#         return C
#
#
# class Rectangle(Figure):
#
#     def __init__(self, name="", a=0, b=0, c=0):
#         super().__init__(name, a, b, c)
#         self.a = a
#         self.b = b
#         self.c = c
#         self.name = name
#
#     def perimeter(self, self.a, self.b, self.c):
#         self.a = a
#         self.b = b
#         self.c = c
#         return a+b+c
#
#
# T = Triangle("T1", a=2, b=6, c=4)
# # T = Circle("C1", r=5)
# # T = Rectangle("R1", a=5, b=4)
# print(T.square())
# print(T.name)
# print(T.perimeter())
#
# # square1 = Rectangle("square1", a=4, b=6)
# # print(square1.square())
#
# # circles = [Circle(name=f'r={i}', r=i) for i in range(1, 5)]
# # rectangles = [Rectangle(name=f'a={i}, b={i**2}', a=i, b=i**2) for i in range(1, 5)]
# # triangles = [Triangle(name=f'a={i+1}, b={i**2}, c={(i + i**2)//2}', a=i+1, b=i**2, c=(i + i**2)//2) for i in range(1, 4)]
# # print(triangles)
# # figures = circles + triangles + rectangles
# # for figure in figures:
# #     print(f'My name is: {figure}')
# #     assert str(figure) == f'{figure.__class__.__name__}:"{figure.name}"'
# #     print(f'My perimeter is: {figure.perimeter()}')
# #     print(f'My square is: {figure.square()}', end=f"\n{'-'*35}\n")
# #
# # assert Circle(name='1', r=2) == Circle(name='2', r=2)
# # assert Circle(name='1', r=2) < Circle(name='2', r=4)
# # assert Circle(name='1', r=4) >= Circle(name='2', r=4)
# #
# #
# # assert Rectangle(name='1', a=2, b=3) == Rectangle(name='2', b=2, a=3)
# # assert Rectangle(name='1', a=2, b=3) < Rectangle(name='2', a=4, b=10)
# # assert Rectangle(name='1', a=4, b=2) >= Rectangle(name='2', a=4, b=1)
# #
# # assert Triangle(name='1', a=2, b=3, c=4) == Triangle(name='2', b=2, a=3, c=4)
# # assert Triangle(name='1', a=2, b=3, c=1.5) < Triangle(name='2', a=4, b=10, c=7)
# # assert Triangle(name='1', a=4, b=2, c=5) >= Triangle(name='2', a=4, b=5, c=1)
#
#

import functools
from math import pi


@functools.total_ordering
class Figure:
        def __init__(self, name=""):
            self.name = name

        def square(self):
            return self.a * self.b

        def perimeter(self):
            return self.a*2 + self.b*2

        def __name__(self):
            return self.name

        def __str__(self):
            return f'{self.__class__.__name__}:"{self.__name__}"'

        def __eq__(self, other):
            return self.square == other.square

        def __lt__(self, other):
            return self.square < other.square


class Triangle(Figure):

    def __init__(self, a=0, b=0, c=0):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        s = (self.a + self.b + self.c)/2
        p = s*(s-self.a)*(s-self.b)*(s-self.c)
        f = p**0.5
        return f

    def perimeter(self):
        return self.a + self.b + self.c


class Circle(Figure):

    def __init__(self, r=0):
        self.radius = r
        super(Circle, self).__init__()

    def square(self):
        return float((pi * self.radius) ** 2)

    def perimeter(self):
        d = self.radius*2
        C = pi*d
        return C


class Rectangle(Figure):

    def __init__(self, a=0, b=0):
        super(Rectangle, self).__init__()
        self.a = a
        self.b = b


R = Rectangle(a=4,b=4)
print(R.square(), R.perimeter())
C = Circle("c1", 5)
print(C.perimeter())
T = Triangle(5, 6, 7)
print(T.perimeter(), T.square())