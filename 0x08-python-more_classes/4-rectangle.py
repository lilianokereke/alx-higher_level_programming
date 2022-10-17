#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """initializing the rectangle class

        Args:
            width(int): The width of the rectangle
            Height(int): The height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):

        """Get/set the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """An area method"""
        return self.__height * self.__width


    def perimeter(self):
        """A perineter method"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    """
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        s = [print("#" * self.__width) for i in range(self.__height)]
        print()
        return("".join(s))
    """
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
