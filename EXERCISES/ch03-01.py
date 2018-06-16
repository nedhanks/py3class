#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys


# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """

    pres_last = []
    with open("./DATA/presidents.txt") as pres_in:
        for pres_line in pres_in:
            pres_data = pres_line.rstrip()
            pres_items = pres_data.split(":")
            pres_last.append(pres_items[1])
        pres_upper = [ p.upper() for p in pres_last ]
        for p in pres_upper:
            print(p)


if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()