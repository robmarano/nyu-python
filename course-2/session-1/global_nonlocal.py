#!/usr/bin/env python3

def changeme(x):
    print('changeme(): x = {}'.format(x))
    x = 10
    print('changeme(): x = {}'.format(x))
    print('changeme(): a = {}'.format(a))
    return

def changeme2(x):
    print('changeme(): x = {}'.format(x))
    x = 10
    print('changeme(): x = {}'.format(x))
    return x

def fact(n):
    """Return the factorial of the given number."""
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r

def fact_recursive(n):
    """Return factorial of given number, generated recursively."""
    if n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)

def fun():
    global a
    b = "bar"
    print('top fun(): a = {}'.format(a))
    print('top fun(): b = {}'.format(b))
    def fun_inner():
        global a
        nonlocal b
        print('before fun_inner(): a = {}'.format(a))
        print('before fun_inner(): b = {}'.format(b))
        a = 100
        b = 50
        print('after fun_inner(): a = {}'.format(a))
        print('after fun_inner(): b = {}'.format(b))
        return
    print('before fun(): a = {}'.format(a))
    print('before fun(): b = {}'.format(b))
    fun_inner()
    a = 1
    b = 2
    print('in fun(): a = {}'.format(a))
    print('in fun(): b = {}'.format(b))
    fun_inner()
    return

def mainline():
    a = "one"
    b = "two"
    print('main(): before fun a = {}'.format(a))
    print('main(): before fun b = {}'.format(b))
    fun()
    print('main(): after fun a = {}'.format(a))
    print('main(): after b = {}'.format(b))

if __name__ == '__main__':
    a = "foo"
    mainline()

    

'''
    a = 1
    print('First, a = {}'.format(a))
    changeme(a)
    print('Second, a = {}'.format(a))
    a = changeme2(a)
    print('Third, a = {}'.format(a))

    n = 100
    r = fact(n)
    print('Factorial of {} = {}'.format(n, r))

    r = fact_recursive(n)
    print('Factorial (recursive) of {} = {}'.format(n, r))
'''
