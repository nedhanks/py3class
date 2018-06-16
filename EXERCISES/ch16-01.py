#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys
import re

# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)

def big_word(m):
    return "*{m.group(0}*"

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """

    with open("../DATA/parrot.txt") as p_in:
        d = p_in.read()
    p_in.close()

    print(d)
    print(60 * '-')
    print('\n')

    eight_plus = re.compile(r'\b(?P<bw>[-a-z]{8,})\b', flags=re.I)
    r = eight_plus.sub("** \g<bw> **", d)

    print(r)

    b_out = open("bigwords.txt", "w")
    b_out.write(r)
    b_out.close()

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
