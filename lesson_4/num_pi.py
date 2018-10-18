# num_pi.py
def fun(n):
    import math
    return f'{math.pi:.{n}f}' # >= 3.6

if __name__ == '__main__':
    print(fun(6))


