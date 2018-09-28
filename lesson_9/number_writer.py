# number_writer.py
import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

# как записать в обычный текстовый файл?
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
