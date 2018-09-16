# new_list.py
from math import sqrt

lst = [2, 4, 9, 16, 25]
new_lst = []

# 1)
for i in lst:
    new_lst.append(sqrt(i))    
print(new_lst)

# 2)
print(list(map(sqrt, lst)))

# 3)
print([sqrt(i) for i in lst])
