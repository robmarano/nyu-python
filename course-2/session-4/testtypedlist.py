#!/usr/bin/env python3

import unittest
from typedlist import TypedList

class TestTypedList(unittest.TestCase):
    def setUp(self):
        self.a_typedlist = TypedList(1, [1,2,3])

    def testGetItem(self):
        self.assertEqual(self.a_typedlist[1],2)

    def testSetItem(self):
        self.a_typedlist[1] = 3
        self.assertEqual(self.a_typedlist[1],3)

if __name__ == '__main__':
    unittest.main()

