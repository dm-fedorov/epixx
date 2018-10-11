# my_max.py
def my_max(a, b):
    ''' Определяет большее из двух чисел '''
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a

print("Введите два числа")
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
print("Из двух введенных большее:", my_max(num1, num2))

