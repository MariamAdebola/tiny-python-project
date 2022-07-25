"""
Author: Mariam Adebola
Date: 23rd July 2022
Aim: Say Hello
"""

#!/usr/local/programs /usr/bin/python

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='Name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Get the main function"""
    args = get_args()
    name = args.name

    print('Hello' + ' ' + name + '!')


main()
