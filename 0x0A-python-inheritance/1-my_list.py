#!/usr/bin/python3

'''Module contain a class with it inheritance.'''


class MyList(list):
    '''A class MyList that inherits from list.'''
    def print_sorted(self):
        my_list = self.copy()
        print(sorted(my_list))
