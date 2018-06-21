#!/usr/bin/env python3

from abc import abstractmethod, ABC

class Shape(ABC):
    ''' Shape class '''
    def __init__(self):
        ''' Shape constructor '''
        super().__init__(self)
        pass

    @abstractmethod
    def area(self):
        ''' calculate area for Shape subclassed object '''
        pass

