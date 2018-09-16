# random_letter1.py
import random

def change_letter_str(word, letter, symbol):
    '''
    Функция заменяет букву letter в слове word на symbol.
    '''
    lst = list(word)
    i = word.index(letter)
    lst[i] = symbol
    return ''.join(lst)

words = ['самовар', 'весна', 'лето']

one_word = random.choice(words)
letter = random.choice(one_word)

print(change_letter_str(one_word, letter, '?'))

user_letter = input("Введите букву:")

if user_letter == letter:
    print("Победа!")
    print("Слово:", one_word)
else:
    print("Увы! Попробуйте в другой раз.")
    print("Слово:", one_word)
