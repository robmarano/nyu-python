#!/usr/bin/env python3

class TypedList:
    ''' List-like class that allows only a single type of item '''
    def __init__(self, example_element, initial_list = []):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must " 
                            "be a list.")
        for element in initial_list: 
            self.__check(element)
        self.elements = initial_list[:]
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of " 
                            "incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element
    def __getitem__(self, i):
        return self.elements[i]
    def __str__(self):
        to_string = '{}'.format(self.elements)
        return to_string
