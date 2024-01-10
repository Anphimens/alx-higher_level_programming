#!/usr/bin/python3
# 0-rectangle.py
"""Empty Class called Rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.

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

    def __str__(self):
        if self.width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        print("Bye rectangle...")
