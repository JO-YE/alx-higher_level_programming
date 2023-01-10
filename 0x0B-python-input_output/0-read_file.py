#/usr/bin/python3
'''Tasks on input/output functions.'''


def read_file(filename=""):
    '''A function that reads a text file and prints it to stdout.'''
    with open(filename, encoding='UTF8') as f:
        print(f.read())
