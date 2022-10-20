#!/usr/bin/python3
"""A rectangle class (blueprint).
"""


class Rectangle:
    """
    A class (blueprint) to create a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Method to get the width of the triangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method to set the width of the rectangle
         Args:
            value (int): a set width value.
        Returns:
            The width value of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Method to get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method to set the height of the rectangle
         Args:
            value (int): a set height value.
        Returns:
            The height value of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Method to compute the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Method to compute the parameter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2*(self.__width + self.height))

    def __str__(self):
        """
        A method that generates a rectangle using '#'
        Returns:
            rect: a rectangle generated from a user defined height and width
        """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return ("")

        else:
            for self.length in range(self.__height):
                rect += (str(self.print_symbol) * self.__width) + "\n"

            return ("".join(rect[:-1]))

    def __repr__(self):
        """
        A module to recreate the rectangle.
        Returns:
            string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        The method finds th largest of the areas of two rectangles
        Args:
            rect_1 (int): the dimensions of rectangle 1
            rect_2 (int): the dimensions of rectangle 2
        """
        if not (isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        return max(rect_1.area(),rect_2.area())
