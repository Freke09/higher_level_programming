#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    Returns the number of characters written.
    Args:
    filename: file to write to
    text: content of the file
    """

    with open(filename, 'w', encoding='UTF-8') as file:
        file2 = file.write(text)
        return (file2)
