# game_num.py
import random

random_num = random.randint(1, 10)
print("Компьютер загадал число.")

count_max = 3
print("У вас есть три попытки. Удачи!")
count = 0

while True:
    user_num = int(input("Попробуйте угадать: "))

    if random_num == user_num:
        print("Победа!")
        break
    else:
        count = count + 1
        if count < count_max:
            if random_num > user_num:
                print("Попробуйте число больше!")
            else:
                print("Попробуйте число меньше!")
        else:
            print("Game over!")
            print("Число:", random_num)
            break
