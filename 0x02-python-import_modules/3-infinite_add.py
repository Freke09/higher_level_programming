#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argsLen = len(argv)
    result = 0
    for i in range(1, argsLen):
        result += int(argv[i])
    print("{}".format(result))
