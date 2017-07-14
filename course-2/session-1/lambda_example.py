#!/usr/bin/env python3

# an anonymous function
# lamdba param1, param2, ..., paramN: expression

def c_to_f(deg_c):
    deg_f = (9/5*deg_c) + 32
    return deg_f

def f_to_c(deg_f):
    deg_c = (deg_f - 32)*5/9
    return deg_c

if __name__ == '__main__':
    deg_f = 24
    deg_c = f_to_c(deg_f)
    print(deg_c)
    
    t = {'FtoC': f_to_c, 'CtoF': c_to_f}
    print(t['FtoC'](32))
    print(t['CtoF'](32))

    t2 = {'FtoC': lambda deg_f: (deg_f - 32)*5/9,
        'CtoF': lambda deg_c: (9/5*deg_c) + 32}
    print(t2['FtoC'](32))
    print(t2['CtoF'](32))
    
