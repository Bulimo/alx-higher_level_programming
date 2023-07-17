#!/usr/bin/python3
"""
test_rectangle module

Tests for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
import pep8


class testRectangle(unittest.TestCase):
    """
    Defines methods to test the Rectangle class
    """

    @classmethod
    def setUpClass(cls):
        """
        Create an instance of the Rectangle class
        """

        print("\nset up")
        cls.rec1 = Rectangle(3, 4, 5, 6)
        cls.rec2 = Rectangle(3, 4)
        cls.rec3 = Rectangle(3, 4, 5, 6, 120)
        cls.rec4 = Rectangle(3, 4, 5)
        cls.rec5 = Rectangle(3, 4, 5, 6)

    @classmethod
    def tearDownClass(cls):
        """
        Clears the instances created
        """

        print("tear down\n")
        cls.rec1 = None
        cls.rec2 = None
        cls.rec3 = None
        cls.rec4 = None
        cls.rec5 = None

    def test_object_created(self):
        """
        confirms an object instance is created
        """

        self.assertTrue(self.rec1)
        self.assertTrue(self.rec2)
        self.assertTrue(self.rec3)
        self.assertTrue(self.rec4)
        self.assertTrue(self.rec5)

    def test_rec_id_value(self):
        """
        tests on the value of public instance id
        """

        self.assertEqual(self.rec3.id, 120)

    def test_instance_attr_value(self):
        """
        tests on the value of private instance width, height, x and y
        """

        self.assertEqual(self.rec1.width, 3)
        self.assertEqual(self.rec2.height, 4)
        self.assertEqual(self.rec2.x, 0)
        self.assertEqual(self.rec2.y, 0)
        self.assertEqual(self.rec4.x, 5)

    def test_private_attribute(self):
        """
        confirms width, height, x and y are private instance attribute
        """

        self.assertTrue('__width' not in self.rec1.__dict__.keys())
        self.assertTrue('width' not in self.rec1.__dict__.keys())
        self.assertTrue('height' not in self.rec1.__dict__.keys())
        self.assertTrue('__height' not in self.rec1.__dict__.keys())
        self.assertTrue('__x' not in self.rec1.__dict__.keys())
        self.assertTrue('x' not in self.rec1.__dict__.keys())
        self.assertTrue('__y' not in self.rec1.__dict__.keys())
        self.assertTrue('y' not in self.rec1.__dict__.keys())

    def test_updated_attribute_values(self):
        """
        confirms the values of instance attributes can be updated
        """

        self.rec1.id = 20
        self.rec5.id = 77
        self.rec2.x = 7
        self.rec4.y = 7
        self.rec3.width = 7
        self.rec5.height = 7
        self.assertEqual(self.rec1.id, 20)
        self.assertEqual(self.rec5.id, 77)
        self.assertEqual(self.rec2.x, 7)
        self.assertEqual(self.rec4.y, 7)
        self.assertEqual(self.rec3.width, 7)
        self.assertEqual(self.rec5.height, 7)

    def test_width_height_type(self):
        """
        confirms TypeError raised for invalid type
        """

        with self.assertRaises(TypeError) as e:
            self.rec1.width = "23"
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            self.rec1.width = 5.6
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            self.rec1.height = True
            self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_height_value(self):
        """
        confirms ValueError raised for invalid values
        """

        with self.assertRaises(ValueError) as e:
            self.rec1.width = 0
            self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            self.rec1.height = -8
            self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_y_value(self):
        """
        confirms ValueError raised for invalid values
        """

        with self.assertRaises(ValueError) as e:
            self.rec1.x = -10
            self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            self.rec1.y = -8
            self.assertEqual(str(e.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as e:
            self.rec1.x = True
            self.assertEqual(str(e.exception), "x must be an integer")

    def test_rect_area(self):
        """
        confirms area is correctly calculated
        """

        self.assertEqual(self.rec3.area(), 12)
        self.rec3.width = 10
        self.rec3.height = 5
        self.assertEqual(self.rec3.area(), 50)

    def test_rec_display(self):
        """
        confirms output of the display method is correct
        """

        from io import StringIO
        from unittest.mock import patch

        self.rec1.x = 0
        self.rec1.y = 0

        output = "###\n###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.rec1.display()
            self.assertEqual(fake_output.getvalue(), output)

        self.rec1.width = 5
        self.rec1.height = 2
        output = "#####\n#####\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.rec1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_rec_magic_str(self):
        """
        confirms output of the magic method __str__ is correct
        """

        from io import StringIO
        from unittest.mock import patch

        output = "[{:s}] ({:d}) {:d}/{:d} - " \
                 "{:d}/{:d}\n".format(self.rec1.__class__.__name__,
                                      self.rec1.id, self.rec1.x, self.rec1.y,
                                      self.rec1.width, self.rec1.height)
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(self.rec1)
            self.assertEqual(fake_output.getvalue(), output)

        self.rec1.width = 5
        self.rec1.height = 2
        output = "[{:s}] ({:d}) {:d}/{:d} - " \
                 "{:d}/{:d}\n".format(self.rec1.__class__.__name__,
                                      self.rec1.id, self.rec1.x, self.rec1.y,
                                      self.rec1.width, self.rec1.height)
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(self.rec1)
            self.assertEqual(fake_output.getvalue(), output)

        self.rec1.width = 5
        self.rec1.height = 2
        self.rec1.x = 2
        self.rec1.y = 3
        output = "[{:s}] ({:d}) {:d}/{:d} - " \
                 "{:d}/{:d}\n".format(self.rec1.__class__.__name__,
                                      self.rec1.id, self.rec1.x, self.rec1.y,
                                      self.rec1.width, self.rec1.height)
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(self.rec1)
            self.assertEqual(fake_output.getvalue(), output)

    def test_rec_display_with_x_y(self):
        """
        confirms output of the display method is correct
        """

        from io import StringIO
        from unittest.mock import patch

        self.rec1.width = 3
        self.rec1.height = 4
        self.rec1.x = 2
        self.rec1.y = 3
        output = "\n\n\n  ###\n  ###\n  ###\n  ###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.rec1.display()
            self.assertEqual(fake_output.getvalue(), output)

        self.rec1.width = 5
        self.rec1.height = 2
        self.rec1.x = 3
        self.rec1.y = 0
        output = "   #####\n   #####\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.rec1.display()
            self.assertEqual(fake_output.getvalue(), output)

        self.rec1.width = 5
        self.rec1.height = 2
        self.rec1.x = 0
        self.rec1.y = 2
        output = "\n\n#####\n#####\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.rec1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_rec_update_1(self):
        """
        confirms Rectangle correctly updates with updates(self, *args) method
        """

        self.rec1.update(89, 4, 5)
        self.assertEqual(self.rec1.id, 89)
        self.assertEqual(self.rec1.width, 4)
        self.assertEqual(self.rec1.height, 5)

        self.rec1.update(89, 7, 8, 2, 3)
        self.assertEqual(self.rec1.id, 89)
        self.assertEqual(self.rec1.width, 7)
        self.assertEqual(self.rec1.height, 8)
        self.assertEqual(self.rec1.x, 2)
        self.assertEqual(self.rec1.y, 3)

        self.rec1.update(89, 7, 8, 2, 3, 7)
        self.assertEqual(self.rec1.id, 89)
        self.assertEqual(self.rec1.width, 7)
        self.assertEqual(self.rec1.height, 8)
        self.assertEqual(self.rec1.x, 2)
        self.assertEqual(self.rec1.y, 3)

        self.rec1.update()
        self.assertEqual(self.rec1.id, 89)
        self.assertEqual(self.rec1.width, 7)
        self.assertEqual(self.rec1.height, 8)
        self.assertEqual(self.rec1.x, 2)
        self.assertEqual(self.rec1.y, 3)

        with self.assertRaises(TypeError) as e:
            self.rec1.update(89, 2.7, 9, 0, 0)
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            self.rec1.update(89, 2, -5, 0, 0)
            self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            self.rec1.update(89, 2, 6, -7, 0)
            self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as e:
            self.rec1.update(89, 2, 6, 3, True)
            self.assertEqual(str(e.exception), "y must be an integer")

    def test_rec_update_2(self):
        """
        confirms Rectangle updates with updates(*args, **kwargs) method
        """

        self.rec1.update(89, 4, 5, 0, 0)
        self.assertEqual(self.rec1.id, 89)
        self.assertEqual(self.rec1.width, 4)
        self.assertEqual(self.rec1.height, 5)

        self.rec1.update(89, 7, 8, x=2, y=3)
        self.assertEqual(self.rec1.id, 89)
        self.assertEqual(self.rec1.width, 7)
        self.assertEqual(self.rec1.height, 8)
        self.assertEqual(self.rec1.x, 0)
        self.assertEqual(self.rec1.y, 0)

        self.rec1.update(y=3, width=7, height=8, id=9, x=2, z=7)
        self.assertEqual(self.rec1.id, 9)
        self.assertEqual(self.rec1.width, 7)
        self.assertEqual(self.rec1.height, 8)
        self.assertEqual(self.rec1.x, 2)
        self.assertEqual(self.rec1.y, 3)

        self.rec1.update()
        self.assertEqual(self.rec1.id, 9)
        self.assertEqual(self.rec1.width, 7)
        self.assertEqual(self.rec1.height, 8)
        self.assertEqual(self.rec1.x, 2)
        self.assertEqual(self.rec1.y, 3)

        with self.assertRaises(TypeError) as e:
            self.rec1.update(width=2.7)
            self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            self.rec1.update(id=89, width=2, height=-5)
            self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            self.rec1.update(id=89, width=2, y=6, x=-7)
            self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as e:
            self.rec1.update(id=89, width=2, y=True)
            self.assertEqual(str(e.exception), "y must be an integer")

    def test_rec_to_dict(self):
        """
        test the Rectangle to dictionary method
        """

        from io import StringIO
        from unittest.mock import patch

        rec1 = Rectangle(5, 6, 8, 9, 37)
        output = "{'id': 37, 'width': 5, 'height': 6, 'x': 8, 'y': 9}\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(rec1.to_dictionary())
            self.assertEqual(fake_output.getvalue(), output)

        rec1.update(15, 1, 2, 3, 4)
        output = "{'id': 15, 'width': 1, 'height': 2, 'x': 3, 'y': 4}\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            print(rec1.to_dictionary())
            self.assertEqual(fake_output.getvalue(), output)

        recdic = Rectangle(5, 6, 8, 9, 37).to_dictionary()
        rec1 = Rectangle(10, 6)
        rec1.update(**recdic)
        self.assertEqual(str(rec1), '[Rectangle] (37) 8/9 - 5/6')


class TestRecPep8(unittest.TestCase):
    """
    Pep8 for files rectangle.py & test_rectangle.py
    """

    def test_pep8(self):
        """
        Pep8 test
        """

        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Pep8 Errors found')
