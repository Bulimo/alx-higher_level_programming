#!/usr/bin/python3
"""Unittest for __init__()
"""
import unittest
Rectangle = __import__('2-rectangle').Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle1(self):
        x = Rectangle(3, 4)
        self.assertEqual(x.width, 3)
        self.assertEqual(x.height, 4)
        self.assertEqual(x.area(), 12)
        self.assertEqual(x.perimeter(), 14)

    def test_rectangle2(self):
        x = Rectangle()
        self.assertEqual(x.width, 0)
        self.assertEqual(x.height, 0)
        self.assertEqual(x.area(), 0)
        self.assertEqual(x.perimeter(), 0)

    def test_rectangle3(self):
        self.assertRaises(TypeError, Rectangle, '3', 4)

    def test_rectangle4(self):
        # self.assertRaises(ValueError, Rectangle, -3, '4')
        self.assertRaises(TypeError, Rectangle, -3, '4')

    def test_rectangle5(self):
        self.assertRaises(ValueError, Rectangle, 3, -4)

    def test_rectangle6(self):
        x = Rectangle(4)
        self.assertEqual(x.width, 4)
        self.assertEqual(x.height, 0)
        self.assertEqual(x.area(), 0)
        self.assertEqual(x.perimeter(), 0)

