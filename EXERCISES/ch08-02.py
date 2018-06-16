#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys


# other imports  (standard library, standard non-library, local)
import lxml.etree as ET


# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    function1()


# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """

    doc = ET.parse('../DATA/presidents.xml')

    root = doc.getroot()

    for pres in root.findall(".//president"):
        lastname = pres.findtext('name/last')
        firstname = pres.findtext('name/first')
        birthstate = pres.findtext('birthstate')
        print(f"{firstname} {lastname} born in {birthstate}")

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
