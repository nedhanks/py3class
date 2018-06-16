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
    presidents = []
    with open("../DATA/presidents.txt") as pres_in:
        for pres_data in pres_in:
            p = pres_data.rstrip().split(":")
            presidents.append((p[2], p[1], p[3], p[-1]))
    pres_sorted = sorted(presidents, key=lambda pres: pres[2], reverse=True)
    print(pres_sorted, '\n')

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
