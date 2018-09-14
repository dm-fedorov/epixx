# my_abs.py
def my_abs(x):
    """Вычисление абсолютного значения"""
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x

print("Абсолютное значение:", my_abs(-2))

