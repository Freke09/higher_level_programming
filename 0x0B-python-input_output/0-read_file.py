#!/usr/bin/python3
"""
Open and read a text file using UTF8.
Print it to stdout
Prototype: def read_file(filename="")
No need to manage permission or file doesn't exist exception
"""

def read_file(filename=""):
    """ Open and read a text file (UTF8) and prints it to stdout.
    Args:
        filename
    """
    with open(filename, encoding='UTF-8') as file:
        text = file.read()
        print(text, end='')
