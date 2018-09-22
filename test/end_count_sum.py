# end_count_sum.py
result = 0

while True:
    num = input("Введите число или Стоп для выхода: ")
    if num == 'Стоп':
        break
    else:
        if num.isdigit():
            result = result + int(num)
        else:
            print("Ошибка ввода.")
            continue
        
print("Сумма:", result)
