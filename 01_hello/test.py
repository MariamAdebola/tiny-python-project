#!/usr/bin/bash -[v]S

import os
from subprocess import getstatusoutput, getoutput

# give a name to the file
file_name = '.\hello.py'

def test_exists():
    """test if the program exists"""
    assert os.path.isfile(file_name)

def test_runs():
    """run the program using python"""
    hello_program = getoutput(F'python {file_name}')
    assert hello_program == "Hello World!"

def test_executable():
    """run the program by default"""
    hello_program = getoutput(file_name)
    assert hello_program == "Hello World!"

def test_usage():
    """test if the program is reusable"""
    for flag in ["-h", "--help"]:
        return_value, prg = getstatusoutput(f'{file_name} {flag}')
        assert return_value == 0
        assert prg.lower().startswith('usage')

def test_input():
    """test if the program will take more inputs"""
    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            return_value, out = getstatusoutput(f'{file_name} {option} {val}')
            assert return_value == 0
            assert out.strip() == f'Hello {val}!'


# use pytest -xv test.py to run the test