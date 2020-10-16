#!/usr/bin/python3
def ftb(filename="<stdin>", line="1", errorin="handler", error="UnknownError", errortext="Unknown error during handler is working."):
    print("Traceback (most recent call last):");
    print('  File "' + str(filename) + '", line ' + str(line) + ", in " + str(errorin))
    print(str(error) + ": " + str(errortext))
