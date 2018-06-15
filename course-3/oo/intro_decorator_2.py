#!/usr/bin/env python3

def decorate(func):
    print('in decorate function, decorating', func.__name__)
    def wrapper_func(**kwargs):
        print('Executing', func.__name__)
        return func(**kwargs)
    return wrapper_func

@decorate
def myfunction(parameter):
    print(parameter)

if __name__ == '__main__':
    myfunction("hello","world")

    exit(0)
