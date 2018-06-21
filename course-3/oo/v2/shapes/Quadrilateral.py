from abc import ABC, abstractmethod
from shapes import Shape
import logging

class Quadrilateral(Shape):
    ''' Quadrilateral class '''
    def __init__(self):
        ''' Self constructor '''
        super()
        # place Quadrilateral initialization here
        logging.info('Initialized Quadrilateral object')
        pass

    @abstractmethod
    def area(self):
        ''' calculate the area for a Quadrilateral '''
        pass
