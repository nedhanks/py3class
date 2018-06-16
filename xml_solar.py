#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys

import lxml.etree as ET

# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """

    doc = ET.parse('DATA/solar.xml')

    root = doc.getroot()

    for node in root:
        for planet in node:
            print(planet.get('planetname'))
            for moon in planet:
                print(f"\t{moon.text}")

    print('-' * 60)

    for planet in doc.findall('.//planet'):
        print(planet.get('planetname'))
        for moon in planet.findall('moon'):
            print(f">>>> {moon.text}")


if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
