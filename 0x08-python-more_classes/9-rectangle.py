#!/usr/bin/python3
# 0-rectangle.py
"""Empty Class called Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.

        Attributes:
            number_of_isinstances (int): The number of rectangle
                                        instances.
            print_symbol (any type): The symbol used for string
                                        representation.

        Args:
            width (int): The width pf the new rectangle.
            height (int): The height of the new rectangle.

        Methods:
            def __init__(self, width=0, height=0):
                            initialize a new rectangle.

            @property
            def width(self):
                            Retrieves the width of the rectangle.
            @width.setter
            def width(self, value):
                            Sets the width of the rectangle.

            @property
            def height(self):
                            Retrieves the height of the rectangle.
            @height.setter
            def height(self, value):
                            Sets the height of the rectangle.

            def area(self):
                            Calculates and retrieves the area of the rectangle.

            def perimeter(self):
                        Calculate and retrieves the perimeter of the rectangle.

            @staticmethod
            def bigger_or_equal(rect_1, rect_2):
            Return the Rectangle with the greater area.

            Args:
                rect_1 (Rectangle): The first Rectangle.
                 (Rectangle): The second Rectangle.
            Raises:
                TypeError: If either of rect_1 or rect_2 is not a Rectangle.

            @classmethod
            def square(cls, size=0):
            Return a new Rectangle with width and height equal to size.
                                    return (cls(size, size))

            Args:
            size (int): The width and height of the new Rectangle.

            def __str__(self):
                        returns the printable representation of the rectangle
                        prints the rectangle with the character #

            def __repr__(self):
                return the string representation of the rectangle

            def __del__(self):
                print the message "Bye rectangle..."

    The `__str__` method is a special method in Python that is called by the
    `str()` built-in function and the `print()` function. It should return a
    human-readable string representation of the object.

        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height for the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This is a public instance that returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * ((self.__width) + (self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    def __str__(self):
        if self.width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
