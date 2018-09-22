# random_letter.py
import random

words = ['самовар', 'весна', 'лето']

one_word = random.choice(words)
print(one_word)

letter = random.choice(one_word)
print(letter)

print(list(one_word))
print(one_word.index(letter))

# пишем функцию:
def change_letter_str(word, letter, symbol):
    '''
    Функция заменяет букву letter в слове word на symbol.
    '''
    lst = list(word)
    i = word.index(letter)
    lst[i] = symbol
    return ''.join(lst)

print(change_letter_str(one_word, letter, '?'))

user_letter = input("Введите букву:")

if user_letter == letter:
    print("Победа!")
    print("Слово:", one_word)
else:
    print("Увы! Попробуйте в другой раз.")
    print("Слово:", one_word)
