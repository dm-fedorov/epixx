# random_letter3.py
import random

words = ['холод', 'снег', 'осень']

one_word = random.choice(words)
letter = random.choice(one_word)

print(one_word.replace(letter, '?'))

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
