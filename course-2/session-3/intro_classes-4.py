#!/usr/bin/env python3

class Temperature:
    def __init__(self):
        self._temp_fahr = 0
    def __del__(self):
        print('In dtor')
    @property
    def temp(self):
        return (self._temp_fahr - 32) * 5 / 9
    @temp.setter
    def temp(self, new_temp):
        self._temp_fahr = new_temp * 9 / 5 + 32

if __name__ == '__main__':
    t = Temperature()
    print(t._temp_fahr)
    print(t.temp)
    t.temp = 34
    print(t.temp)
    print(t._temp_fahr)
    print(t)
