from abc import ABC, abstractmethod
import logging

class Shape(ABC):
    ''' Shape class '''
    def __init__(self):
        ''' Self constructor '''
        super().__init__(self)
        # place Shape initialization here
        logging.info('Initialized Shape object')
        pass

    @abstractmethod
    def area(self):
        ''' calculate the area for a Shape '''
        pass
