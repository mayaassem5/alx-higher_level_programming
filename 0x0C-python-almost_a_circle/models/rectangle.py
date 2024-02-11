#!/usr/bin/python3
"""Module of rectangle"""


from models.base import Base


class Rectangle(Base):
    """Type class of a rectangle inherited from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width function private"""

        return self.__width

    @width.setter
    def width(self, value):
        """width function for setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height function private"""

        return self.__height

    @height.setter
    def height(self, value):
        """height function private"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x function private"""

        return self.__x

    @x.setter
    def x(self, value):
        """x function setter"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y function private"""

        return self.__y

    @y.setter
    def y(self, value):
        """y function setter"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


     def area(self):
        """areat function"""

        return self.width * self.height

    def display(self):
        """display function"""

        [print("") for y in range(self.y)]
        for j in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for k in range(self.width)]
            print("")

    def __str__(self):
        """str function"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """update rectangle attributes
        """

        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)


    def to_dictionary(self):
        """to_dictionary function"""

        return {
            "id": self.id, "width": self.width, "height": self.height,
            "x": self.x,
            "y": self.y,
        }

