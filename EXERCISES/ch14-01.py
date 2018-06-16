#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys


# other imports  (standard library, standard non-library, local)
import openpyxl as px

# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """

    print(px.__version__)

    pb = px.load_workbook('../DATA/computer_people.xlsx')

    for ps in pb:
        print("ws: ", ps)

    people = pb["people"]

    age_range = people['D2':'D9']

    for row in age_range:
        isinstance()




if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
