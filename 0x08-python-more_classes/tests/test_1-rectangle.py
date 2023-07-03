#!/usr/bin/python3
"""Unittest for __init__()
"""
import unittest
Rectangle = __import__('1-rectangle').Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle1(self):
        x = Rectangle(3, 4)
        self.assertEqual(x.width, 3)
        self.assertEqual(x.height, 4)

    def test_rectangle5(self):
        x = Rectangle()
        self.assertEqual(x.width, 0)
        self.assertEqual(x.height, 0)

    def test_rectangle2(self):
        self.assertRaises(TypeError, Rectangle, '3', 4)

    def test_rectangle3(self):
        # self.assertRaises(ValueError, Rectangle, -3, '4')
        self.assertRaises(TypeError, Rectangle, -3, '4')

    def test_rectangle6(self):
        self.assertRaises(ValueError, Rectangle, 3, -4)
