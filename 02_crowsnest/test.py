#!/usr/bin/env python

import os
from subprocess import getstatusoutput, getoutput

FILE_NAME = './crowsnest.py'

consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]

vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']

TEMPLATE = 'Ahoy, Captain, {} {} off the larboard bow!'


def test_exists():
    """test if the program exists"""
    assert os.path.isfile(FILE_NAME)


def test_usage():
    """test if the program is reusable"""
    for flag in ['-h', '--help']:
        return_value, out = getstatusoutput(f'python {FILE_NAME} {flag}')
        assert return_value == 0
        assert out.lower().startswith('usage')

def test_consonant():
    """check for the word "brigantine" """

    for word in consonant_words:
        out = getoutput(f'python {FILE_NAME} {word}')
        assert out.strip() == TEMPLATE.format('an', word)


def test_consonant_upper():
    """check for the word "Brigantine" """

    for word in consonant_words:
        out = getoutput(f'python {FILE_NAME} {word.title()}')
        assert out.strip() == TEMPLATE.format('an', word.title())


def test_vowel():
    """check for the word "octopus" """

    for word in vowel_words:
        out = getoutput(f' python {FILE_NAME} {word}')
        assert out.strip() == TEMPLATE.format('a', word)


def test_vowel_upper():
    """check for the word "Octopus" """

    for word in vowel_words:
        out = getoutput(f' python {FILE_NAME} {word.upper()}')
        assert out.strip() == TEMPLATE.format('a', word.upper())
