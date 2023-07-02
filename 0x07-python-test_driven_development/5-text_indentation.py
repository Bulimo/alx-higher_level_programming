#!/usr/bin/python3
"""
Module 5-text_indentation

Function:
    text_indentation: function that prints text with new line identation
"""


def text_indentation(text):
    """
     A function that prints a text with 2 new lines after each of
      these characters: '.', '?' and ':'

     Args:
        text(str): text is a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        # print(i)
        if text[i] == '.' or text[i] == ':' or text[i] == '?':
            print(text[i])
            print()
            i += 1
            if i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
