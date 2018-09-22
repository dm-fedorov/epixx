# call_tel.py

def get_count_tel(code, time):
    '''Функция, которая по коду города и длительности
       переговоров вычисляет их стоимость'''
    if code == 343: # Екатеринбург
        return time*15
    elif code == 381: # Омск
        return time*18
    elif code == 473: # Воронеж
        return time*13
    elif code == 485: # Ярославль
        return time*11
    else:
        return 0

def get_code_city(city):
    '''Функция, которая по городу определяет его код'''
    if city == "Екатеринбург":
        return 343
    elif city == "Омск":
        return 381
    elif city == "Воронеж":
        return 473
    elif city == "Ярославль":
        return 485
    else:
        return 0

city = input("Укажите город: ")
time = int(input("Укажите время разговора: "))
print('Стоимость составляет', get_count_tel(get_code_city(city), time), 'руб.')

