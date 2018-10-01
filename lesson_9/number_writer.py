# number_writer.py
import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

try:
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)
except:
    print("Что-то пошло не так...")
