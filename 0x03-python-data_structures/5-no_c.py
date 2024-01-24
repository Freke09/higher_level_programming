#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        string1 = my_string.translate({ord("c"): None})
        string2 = string1.translate({ord("C"): None})
        return (string2)
    return (my_string)
