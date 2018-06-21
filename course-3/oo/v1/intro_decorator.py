#!/usr/bin/env python3

def decorate(func):
    print('in decorate function, decorating', func.__name__)
    def wrapper_func(*args):
        print('Executing', func.__name__, args)
        return func(*args)
    return wrapper_func

def myfunction(parameter):
    print(parameter)

if __name__ == '__main__':
    myfunction = decorate(myfunction)
    print(myfunction)

    myfunction("hello")

    exit(0)

