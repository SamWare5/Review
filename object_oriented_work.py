import math
import re


class Shape:

    def __init__(self, color):
        self.__color = color


def get_color(self):
    return self.__color


def set_color(self, color):
    self.__color = color


class Rectangle(Shape):
    __list_of_shape = []

    def __int__(self,  width, length):
        super().__init__()
        self.__width = width
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_area(self):
        return self.__width * self.__length

    def get_perimeter(self):
        return (self.__length + self.__width) * 2


class Square(Shape):

    def __int__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def get_side_length(self):
        return self.__side_length

    def set_side_length(self, side_length):
        self.__side_length = side_length

    def get_area(self):
        return self.__side_length * self.__side_length

    def get_perimeter(self):
        return (self.__side_length + self.__side_length)*2


class Circle(Shape):

    def __int__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return self.math.pi.__self.radius*2


class Shapes:

    def add_shape(self, new_shape: Shape):
        self.__list_of_shape.append[new_shape]

    def delete_shape(self, shape: Shape):
        for x in self.__list_of_shape:
            if re.match([shape], x):
                self.__list_of_shape.remove(shape)


r1 = Rectangle(1.2)
print(r1.get_area())

