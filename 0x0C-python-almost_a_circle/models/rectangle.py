#!/usr/bin/python3
"""
Module rectangle

class:
    Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines class Rectangle that inherits from Base class

    Methods;
        __init__()
        width()
        width.setter()
        height()
        height.setter()
        x()
        x.setter()
        y()
        y.setter()
        display()
        __str__()
        update()

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes an instance of Rectangle object

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x-coordinate of the rectangle
            y: y-coordinate of the rectangle
            id: id value of the object
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter method for width private atttribute
        """

        return self.__width

    @width.setter
    def width(self, val):
        """
        setter method for the width atttribute

        Args:
            val: new value of width of the rectangle
        """

        if type(val) != int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """
        getter method for height private atttribute
        """

        return self.__height

    @height.setter
    def height(self, val):
        """
        setter method for the height atttribute

        Args:
            val: new value of height of the rectangle
        """

        if type(val) != int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """
        getter method for x private atttribute
        """

        return self.__x

    @x.setter
    def x(self, val):
        """
        setter method for the x atttribute

        Args:
            val: new value of x of the rectangle
        """

        if type(val) != int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """
        getter method for y private atttribute
        """

        return self.__y

    @y.setter
    def y(self, val):
        """
        setter method for the y atttribute

        Args:
            val: new value of y of the rectangle
        """

        if type(val) != int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """
        Calculates the area of the rectangle object

        Args:
            None

        Returns:
            width * height
        """

        return self.__width * self.__height

    def display(self):
        """
        prints the size of rectangle using character #
        It also considers the x and y plane values

        Returns:
            None
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print("{:s}{:s}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """
        returns a string representation of the rectangle object
        """

        output = "[{:s}] ({:d}) {:d}/{:d} - " \
                 "{:d}/{:d}".format(self.__class__.__name__, self.id,
                                    self.__x, self.__y, self.__width,
                                    self.__height)
        return output

    def update(self, *args, **kwargs):
        """
        provides for updating the rectangle class

        Args:
            args(int): a varible length of type int arguments

        Returns:
            None
        """

        attr = ["id", "width", "height", "x", "y"]

        if args is not None and len(args) > 0:
            for k, v in enumerate(args):
                if k < len(attr):
                    setattr(self, attr[k], v)
                else:
                    break
        else:
            if kwargs is not None and len(kwargs) > 0:
                for k, v in kwargs.items():
                    if k in attr:
                        setattr(self, k, v)
        """
        Alternative implementation

        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        """

    def to_dictionary(self):
        """
        Represents a triangle object as a dictionary

        Args:
            None

        Returns:
            returns the dictionary representation of a Rectangle class object
        """

        dict_attr = {k: v for k, v in self.__dict__.items()}
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
