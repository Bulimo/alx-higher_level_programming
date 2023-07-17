#!/usr/bin/python3
"""
Module square

class:
    Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines class Square that inherits from Rectangle class

    Methods;
        __init__()
        size()
        size.setter()
        area()
        __str__()
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes an instance of Square object

        Args:
            size(int): size of the square
            x: x-coordinate of the square
            y: y-coordinate of the square
            id: id value of the object
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter method for size private atttribute
        """

        return self.width

    @size.setter
    def size(self, val):
        """
        setter method for the size atttribute

        Args:
            val: new value of size of square
        """

        self.width = val
        self.height = val

    def __str__(self):
        """
        returns a string representation of the rectangle object
        """

        output = "[{:s}] ({:d}) {:d}/{:d} - " \
                 "{:d}".format(self.__class__.__name__, self.id,
                               self.x, self.y, self.width)
        return output

    def update(self, *args, **kwargs):
        """
        provides for updating the Square class

        Args:
            args(int): a varible length of type int arguments
            *kwargs: a dictionary: key/value pairs of attribute values

        Returns:
            None
        """

        attr = ["id", "size", "x", "y"]

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

    def to_dictionary(self):
        """
        Represents a Square object as a dictionary

        Args:
            None

        Returns:
            returns the dictionary representation of a Square class object
        """

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
