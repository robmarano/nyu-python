#from abc import ABC, abstractmethod
from shapes import Quadrilateral
import logging

class Rectangle(Quadrilateral):
    ''' Rectangle class '''
    def __init__(self,length=1, width=1):
        ''' Self constructor '''
        super()
        # place Rectangle initialization here
        logging.info('Initialized Rectangle object')
        self.length = length
        self.width = width
        pass

    def area(self):
        ''' calculate the area for a Rectangle '''
        return (self.length * self.width)
        pass
