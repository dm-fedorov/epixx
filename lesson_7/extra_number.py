# extra_number.py
def total(initial=5, *numbers, extra_number): 
    count = initial 
    for number in numbers: 
        count += number 
    count += extra_number 
    return count

if __name__ == '__main__':
    print(total(10, 1, 2, 3, extra_number=50))
    # Вызовет ошибку, поскольку мы не указали значение 
    # аргумента по умолчанию для extra_number:
    # print(total(10, 1, 2, 3)) 


