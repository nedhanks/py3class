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
    words = ET.Element('words')

    with open('../DATA/words.txt') as words_in:
        for w in words_in:
            if w.startswith('x'):
                word = ET.SubElement(words, 'word').text = w.rstrip()

    print(ET.tostring(words, pretty_print=True).decode())

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
