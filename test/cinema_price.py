# cinema_price.py
def print_all(cinema, day, session, num):
    print('Выбрали фильм:', cinema, 'День:', day, 'Время:', session, 'Количество билетов:', num)   

def price_cinema(cinema, day, session, num):
    """ Определяет стоимость билетов в кино """
    # итоговая стоимость
    result = 0    
    if cinema == "Пятница":
        if session == 12:
            result = 250
        elif session == 16:
            result = 350
        elif session == 20:
            result = 450
        else:            
            return -1 # возвращаем в случае ошибки
    elif cinema == "Чемпионы":
        if session == 10:
            result = 250
        elif session == 13:
            result = 350
        elif session == 16:
            result = 350
        else:
            return -1 # возвращаем в случае ошибки
    elif cinema == "Пернатая банда":
        if session == 10:
            result = 350
        elif session == 14:
            result = 450
        elif session == 18:
            result = 450
        else:
            return -1 # возвращаем в случае ошибки
    else:    
        return -1 # возвращаем в случае ошибки
    # количество билетов
    result = num * result
    # скидка
    if num >= 20:
        result = result-result*0.2
    if day == "завтра":
        result = result-result*0.05
    return result

print("Программа для подсчета стоимости билетов в кино.")
c = input("Выбрать фильм: ")
d = input("Выбрать день (сегодня, завтра): ")
t = int(input("Выбрать время: "))
n = int(input("Выбрать количество билетов: "))    
print_all(c, d, t, n)
result = price_cinema(c, d, t, n)
if result == -1:
    print("Ошибка ввода.")
else:
    print("Результат:", result, 'руб.')



