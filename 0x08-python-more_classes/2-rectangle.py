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
        if self._width == 0 or self._height == 0:
            return 0
        return (self.__height + self.__width) * 2
