#!/usr/bin/env python3

class Temperature:
    def __init__(self):
        self._temp_fahr = float(0)
        self._temp_celc = float(0)
    @property
    def temp(self):
        #return (self._temp_fahr - 32) * 5 / 9
        return (self._temp_celc)
    @temp.setter
    def temp(self, new_temp):
        self._temp_celc = float(new_temp)
        self._temp_fahr = new_temp * 9 / 5 + 32

if __name__ == '__main__':
    t = Temperature()
    print(t._temp_fahr)
    print(t.temp)
    t.temp = 34
    a = t.temp
    t.temp = 12
    print(a)
    print(type(a))
    print(t._temp_fahr)

