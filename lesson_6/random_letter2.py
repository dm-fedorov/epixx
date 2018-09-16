# random_letter2.py
import random

def change_letter_str(word, letter, symbol):
    '''
    Функция заменяет букву letter в слове word на symbol.
    '''
    lst = list(word)    

    for i in range(len(lst)):
        if lst[i] == letter:
            lst[i] = symbol

    return ''.join(lst)

words = ['холод', 'снег', 'осень']

one_word = random.choice(words)
letter = random.choice(one_word)

# print(change_letter_str('холод', 'о', '?'))
print(change_letter_str(one_word, letter, '?'))

# попытки
max_count = 3
print("В игре 3 попытки.")
count = 0

while True:
    user_letter = input("Введите букву:")

    if user_letter == letter:
        print("Победа!")
        print("Слово:", one_word)
        break
    else:
        print("Увы!")        
        count = count + 1
        if count >= max_count:
            print("Увы! Попробуйте в другой раз.")
            print("Слово:", one_word)
            break           
