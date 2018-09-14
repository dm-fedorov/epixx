# my_func_sinus.py
from math import sin

def fun(x):
    if 0.2 <= x <= 0.9:
        return sin(x)
    else:
        return 1

print(fun(0.4))


