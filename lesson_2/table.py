# table.py
value = input("Введите атомный номер элемента: ")
if len(value) > 0:
    num = int(value)
    if num == 3:        
        print("Li, Литий")
    elif num == 17:
        print("Cl, Хлор")
    elif num == 25:
        print("Mn, Марганец")
    elif num == 80:
        print("Hg, Ртуть")        
    else:
        print("Не могу определить, что это")
else:
    print("Введите значение.")
