#!/usr/bin/env python3
""" a list that only allows items of a single type
any text (like this) that isn't in shell format is ignored by doctest

>>> from typedlist_doctest import TypedList
>>> a_typed_list = TypedList(1, [1,2,3])
>>> a_typed_list[1] == 2
True
>>> a_typed_list[1] = 3
>>> a_typed_list[1]
3
>>>
"""
# >>> print([1,2,3,4]) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
# This matches all of the following:
# [1,    2,   3,              4]
# [1,    2,
#    3, 4]
# [1, ... 4]

class TypedList:
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
