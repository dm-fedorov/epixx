# get_parity.py
def get_parity(a):
    ''' Проверка числа на четность '''
    if a%2 == 0:
        return "четное"
    else:
        return "нечетное"

num = int(input("Введите число: "))
print("Число", num, get_parity(num))

