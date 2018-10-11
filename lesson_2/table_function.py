# table.py
def get_element(val):
    if len(val) > 0:
        num = int(val)
        if num == 3:        
            return "Li, Литий"
        elif num == 17:
            return "Cl, Хлор"
        elif num == 25:
            return "Mn, Марганец"
        elif num == 80:
            return "Hg, Ртуть"
        else:
            return "Не могу определить, что это"
    else:
        return "Введите значение"

value = input("Введите атомный номер элемента: ")
print(get_element(value))



