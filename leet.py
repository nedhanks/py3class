#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys


# other imports  (standard library, standard non-library, local)
#import str

# constants (AKA global variables -- keep these to a minimum)

a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY2"
l = "46cd3f6h19k1mn0pqr57uvwxyz4BCD3F6H19K1MN0PQRS7UVWXY2"
n = "1234567890"

t = str.maketrans(a, l)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    prompt = "> "
    s = input(prompt)
    print((s.translate(t)))

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
