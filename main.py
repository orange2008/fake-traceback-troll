#!/usr/bin/python3
def ftb(filename, line, errorin, error, errortext):
    print("Traceback (most recent call last):");
    print(' File "' + filename + '", line ' + line + ", in " + errorin)
    print(error + ": " + errortext)

