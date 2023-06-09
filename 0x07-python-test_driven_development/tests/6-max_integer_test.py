#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer1(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer2(self):
        self.assertEqual(max_integer([1, 2, 7, 4, 5]), 7)
        self.assertEqual(max_integer([7, 2, 2, 4, 5]), 7)

    def test_max_integer3(self):
        self.assertEqual(max_integer([-1, -2, 0, -4, -5]), 0)
        self.assertEqual(max_integer([3, -2, 0, -4, -5]), 3)

    def test_max_integer4(self):
        self.assertNotEqual(max_integer([-1, -2, -3, -4, -5]), -5)

    def test_max_integer5(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    def test_max_integer6(self):
        self.assertRaises(TypeError, max_integer, 5)

    def test_max_integer7(self):
        self.assertEqual(max_integer("Peter"), 't')

    def test_max_integer8(self):
        self.assertEqual(max_integer("12345"), '5')

    def test_max_integer9(self):
        self.assertRaises(TypeError, max_integer, False)
        with self.assertRaises(TypeError):
            max_integer([-10, 0.5, "str", {1, 2}])

    def test_max_integer10(self):
        self.assertEqual(max_integer((3, 5)), 5)

    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)
