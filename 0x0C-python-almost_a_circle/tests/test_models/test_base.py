#!/usr/bin/python3
"""
test_base module

Tests for base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import os
import pep8


class testBase(unittest.TestCase):
    """
    Defines methods to test Base Class
    """

    class TestBase(unittest.TestCase):
        """
        Tests for models/base.py
        """

        def setUp(self):
            if os.path.exists("Base.json"):
                os.remove("Base.json")
            if os.path.exists("Rectangle.json"):
                os.remove("Rectangle.json")

        def tearDown(self):
            if os.path.exists("Base.json"):
                os.remove("Base.json")
            if os.path.exists("Rectangle.json"):
                os.remove("Rectangle.json")

    def test_id_value(self):
        """
        Test for given id values
        """

        self.assertTrue(Base(2), self.id == 2)
        self.assertTrue(Base(900), self.id == 900)
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attributes(self):
        """
        confirms __nb_objects is a private attribute
        """

        with self.assertRaises(AttributeError):
            print(Base.nb_objects)
            print(Base.__nb_objects)
        self.assertFalse(hasattr(Base, '__nb_objects'))

    def test_object_created(self):
        """
        confirms object is created
        """

        self.assertTrue(Base(10))

    def test_to_json_string(self):
        """
        Tests given object given is translated into JSON string
        """

        from io import StringIO
        from unittest.mock import patch

        so = '[{"id": 3, "width": 4, "height": 5, "x": 2, "y": 2}]\n'
        r = [{"id": 3, "width": 4, "height": 5, "x": 2, "y": 2}]
        with patch("sys.stdout", new=StringIO()) as out:
            print(Base.to_json_string(r))
            self.assertEqual(out.getvalue(), so)

        so = "[]\n"
        r = None
        with patch("sys.stdout", new=StringIO()) as out:
            print(Base.to_json_string(r))
            self.assertEqual(out.getvalue(), so)

        so = "[]\n"
        r = dict()
        with patch("sys.stdout", new=StringIO()) as out:
            print(Base.to_json_string(r))
            self.assertEqual(out.getvalue(), so)

    def test_save_to_file(self):
        """
        Tests a JSON string representation of an object is saved in file
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(2, 3, 4, 5, 6)

        # Save the instances to file
        Rectangle.save_to_file([r1, r2])
        # Check if the file is created

        self.assertTrue(os.path.exists("Rectangle.json"))
        # Check if the file contains the correct JSON representation

        with open("Rectangle.json", "r") as my_file:
            json_data = json.load(my_file)
            output = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json_data, output)

    def test_save_none_to_file(self):
        """
        Tests a JSON string representation of an object is saved in file
        """

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", mode="r") as my_file:
            output = my_file.read()
            self.assertEqual("[]", output)

    def test_save_empty_to_file(self):
        """
        Tests a JSON string representation of an object is saved in file
        """

        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", mode="r") as my_file:
            output = my_file.read()
            self.assertEqual("[]", output)

    def test_create(self):
        """
        Test creation of Python Object from dictioanry
        """

        r1 = Rectangle(3, 5, 1, 2, 99)
        r = r1.to_dictionary()
        r2 = Rectangle.create(**r)
        self.assertEqual(str(r1), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(r, r2)

    def test_load_from_file(self):
        """
        confirm that object is created from file
        """

        r = Rectangle(3, 4, 2, 8, 10)
        Rectangle.save_to_file([r])
        rdic = Rectangle.load_from_file()
        self.assertEqual(str(rdic), '[Rectangle] (10) 2/8 - 3/4')

    def test_load_from_empty_file(self):
        with open("Rectangle.json", "w") as file:
            pass
        instances = Rectangle.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_nonexistent_file(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_from_json_string(self):
        json_string = '[{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}]'
        dict_list = Base.from_json_string(json_string)
        output = [{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}]
        self.assertEqual(dict_list, output)

    def test_from_json_string_with_empty_list(self):
        json_string = '[]'
        dict_list = Base.from_json_string(json_string)
        self.assertEqual(dict_list, [])

    def test_from_json_string_with_none(self):
        dict_list = Base.from_json_string(None)
        self.assertEqual(dict_list, [])


class TestPep8(unittest.TestCase):
    """
    Pep8 for files base.py & test_base.py
    """

    def test_pep8(self):
        """
        Pep8 test
        """

        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')
