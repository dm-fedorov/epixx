# random_game.py
import random

print("Угадайка")
num = random.randint(1, 7)
user_num = int(input("Введите число от 1 до 7: "))
if user_num == num:
    print("Победа!")
else:
    print("Повторите еще раз!")
    print("ПК загадал число ", num) 
