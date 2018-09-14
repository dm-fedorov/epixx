# geron.py
def geron(a, b, c): 
    ''' Вычисляет площадь треугольника по формуле Герона '''
    import math
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
  
if __name__ == "__main__":
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))
    print("Площадь треугольника по формуле Герона:", geron(a, b, c))

