#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys

# other imports  (standard library, standard non-library, local)

from president import President


# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    # !/usr/bin/env python
    for term in 1, 26, 39, 45:
        p = President(term)  # George Washington

        print("{0} {1} was born at {2}, {3} on {4}".format(
            p.first_name, p.last_name, p.birth_place, p.birth_state, p.birth_date
        ))
        print()


if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
