# two_random_game.py
from random import randint

# игроки начинают играть
num1 = randint(1, 6)
num2 = randint(1, 6)

if num1 > num2:
    print("Победил первый игрок!")
elif num1 < num2:
    print("Победил второй игрок!")
else:
    print("Ничья!")

