# value_cinema.py

def value_cinema(hall, session, num):
    """ Определяет стоимость билетов в кино """
    # итоговая стоимость
    result = 0
    # стоимость сеансов
    if hall == "Красный":
        if session == 12:
            result = 250
        elif session == 16:
            result = 350
        elif session == 20:
            result = 450
    elif hall == "Синий":
        if session == 10:
            result = 250
        elif session == 13:
            result = 350
        elif session == 16:
            result = 350
    elif hall == "Голубой":
        if session == 10:
            result = 350
        elif session == 14:
            result = 450
        elif session == 18:
            result = 450        
    # количество билетов
    result = num * result
    # скидка
    if 5 < num < 10:
        result = result-result*0.05
    elif num > 10:
        result = result-result*0.1
    return result

hall = input("Укажите зал (Красный, Синий, Голубой):")
session = int(input("Укажите сеанс (10, 12, 13, 14, 16, 18, 20): "))
num = int(input("Укажите количество билетов:"))
print("Итог с учетом скидки:", value_cinema(hall, session, num), 'руб.')
