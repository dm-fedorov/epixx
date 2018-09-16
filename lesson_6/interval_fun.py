# interval_fun.py
from operator import add 

result = 0

for x in range(10, 31, 2):
    result = result + add(pow(x, 2), 3)

print(result)
