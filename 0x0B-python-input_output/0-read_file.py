#!/usr/bin/python3

def read_file(filename=""):
    """ Read a text file (UTF8) and prints it to stdout """
    with open(filename, encoding='UTF-8') as file:
        text = file.read()
        print(text, end='')
