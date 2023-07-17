#!/usr/bin/python3
"""
test_square module

Tests for Rectangle class
"""
import unittest
from models.square import Square
import pep8


class test_Square(unittest.TestCase):
    """
    Defines methods to test the Squaree class
    """

    def test_square_created(self):
        """
        confirms an object instance is created
        """
        s1 = Square(5)
        s2 = Square(5, 2, 2)
        s3 = Square(5, 2, 2, 7)
        self.assertTrue(s1)
        self.assertTrue(s2)
        self.assertTrue(s3)

    def test_square_id_value(self):
        """
        tests on the value of public instance id
        """

        s3 = Square(5, 2, 2, 7)
        self.assertEqual(s3.id, 7)

    def test_square_attr_value(self):
        """
        tests on the value of private instance width, height, x and y
        """

        s1 = Square(5)
        s2 = Square(5, 2, 2)
        s3 = Square(5, 0, 0, 7)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 0)
        self.assertEqual(s3.x, 0)

    def test_updated_square_attribute(self):
        """
        confirms the values of instance attributes can be updated
        """

        s1 = Square(5)
        s1.id = 20
        s1.width = 77
        s1.height = 77
        s1.x = 7
        s1.y = 7
        self.assertEqual(s1.id, 20)
        self.assertEqual(s1.width, 77)
        self.assertEqual(s1.height, 77)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 7)

    def test_square_width_height_type(self):
        """
        confirms TypeError raised for invalid type
        """

        s1 = Square(5, 2, 2, 7)
        with self.assertRaises(TypeError) as e:
            s1.width = "23"
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            s1.width = 5.6
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            s1.height = True
            self.assertEqual(str(e.exception), "height must be an integer")

    def test_square_width_height_value(self):
        """
        confirms ValueError raised for invalid values
        """

        s1 = Square(5, 2, 2, 7)
        with self.assertRaises(ValueError) as e:
            s1.width = 0
            self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            s1.height = -8
            self.assertEqual(str(e.exception), "height must be > 0")

    def test_square_x_y_value(self):
        """
        confirms ValueError raised for invalid values
        """

        s1 = Square(5, 2, 2, 7)
        with self.assertRaises(ValueError) as e:
            s1.x = -10
            self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            s1.y = -8
            self.assertEqual(str(e.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as e:
            s1.x = True
            self.assertEqual(str(e.exception), "x must be an integer")

    def test_square_area(self):
        """
        confirms area is correctly calculated
        """

        s1 = Square(5, 2, 2, 7)
        self.assertEqual(s1.area(), 25)
        s1.width = 10
        s1.height = 10
        self.assertEqual(s1.area(), 100)

    def test_square_display(self):
        """
        confirms output of the display method is correct
        """

        from io import StringIO
        from unittest.mock import patch

        s1 = Square(3)
        output = "###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            s1.display()
            self.assertEqual(fake_output.getvalue(), output)

        s1.width = 5
        s1.height = 5
        output = "#####\n#####\n#####\n#####\n#####\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            s1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_square_magic_str(self):
        """
        confirms output of the magic method __str__ is correct
        """

        from io import StringIO
        from unittest.mock import patch

        s1 = Square(3, 0, 0, 6)
        output = "[Square] (6) 0/0 - 3\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(s1)
            self.assertEqual(fake_output.getvalue(), output)

        s1.width = 5
        s1.height = 5
        output = "[Square] (6) 0/0 - 5\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(s1)
            self.assertEqual(fake_output.getvalue(), output)

        s1.width = 5
        s1.height = 5
        s1.x = 2
        s1.y = 3
        s1.id = 19
        output = "[Square] (19) 2/3 - 5\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(s1)
            self.assertEqual(fake_output.getvalue(), output)

    def test_square_display_with_x_y(self):
        """
        confirms output of the display method is correct
        """

        from io import StringIO
        from unittest.mock import patch

        s1 = Square(4, 2, 3)
        output = "\n\n\n  ####\n  ####\n  ####\n  ####\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            s1.display()
            self.assertEqual(fake_output.getvalue(), output)

        s1.width = 5
        s1.height = 5
        s1.x = 3
        s1.y = 0
        output = "   #####\n   #####\n   #####\n   #####\n   #####\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            s1.display()
            self.assertEqual(fake_output.getvalue(), output)

        s1.width = 3
        s1.height = 3
        s1.x = 0
        s1.y = 2
        output = "\n\n###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            s1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_square_size(self):
        """
        test and confirm size correctly updates width and height
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.area(), 100)

        with self.assertRaises(TypeError) as e:
            s1.size = "23"
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            s1.size = None
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = -7
            self.assertEqual(str(e.exception), "width must be an integer")

    def test_square_update(self):
        """
        confirms Square updates with updates(*args, **kwargs) method
        """

        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.area(), 25)

        s1.update(89, 4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.area(), 16)

        s1.update(89, 8, x=2, y=3)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.area(), 64)

        s1.update(y=3, size=8, id=9, x=2, z=7)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.area(), 64)

        s1.update()
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.area(), 64)

        with self.assertRaises(TypeError) as e:
            s1.update(size=2.7)
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.update(id=89, size=-5)
            self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            s1.update(id=89, size=2, y=6, x=-7)
            self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as e:
            s1.update(id=89, size=2, y=True)
            self.assertEqual(str(e.exception), "y must be an integer")

    def test_square_to_dict(self):
        """
        test the square to dictionary method
        """

        from io import StringIO
        from unittest.mock import patch

        s2 = Square(23, 8, 2, 10)
        output = "{'id': 10, 'size': 23, 'x': 8, 'y': 2}\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(s2.to_dictionary())
            self.assertEqual(fake_output.getvalue(), output)

        s2.update(2, 10, 3, 7)
        output = "{'id': 2, 'size': 10, 'x': 3, 'y': 7}\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(s2.to_dictionary())
            self.assertEqual(fake_output.getvalue(), output)

        s = Square(6, 8, 9, 37).to_dictionary()
        s3 = Square(10, 6)
        s3.update(**s)
        self.assertEqual(str(s3), '[Square] (37) 8/9 - 6')


class TestRecPep8(unittest.TestCase):
    """
    Pep8 for files square.py & test_square.py
    """

    def test_pep8(self):
        """
        Pep8 test
        """

        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Pep8 Errors found')
