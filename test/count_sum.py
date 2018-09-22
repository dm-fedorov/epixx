# count_sum.py
num = input("Введите число: ")
result = 0

for i in num:
    if not int(i)%2:
        result = result + pow(int(i), 2)

print("Результат:", result)
