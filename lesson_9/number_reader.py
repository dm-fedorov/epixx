# number_reader.py
import json

filename = 'numbers.json'

try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)

    print(numbers)
except:
    print("Упс. Что-то пошло не так.")
