"""
Author : Mariam Adeoti
Date   : July 23rd 2022
Purpose: choose the right article
"""

import argparse

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')


    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    article = 'a' if word[0].lower() in 'aeiou' else 'an'

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


if __name__ == '__main__':
    main()