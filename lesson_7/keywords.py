# keywords.py
def total(initial=5, *numbers, **keywords):    
    count = initial 
    for number in numbers: 
        count += number 
    for key in keywords: 
        count += keywords[key] 
    return count 

print(total()) # initial=5
print(total(2, 1)) # initial=2
print(total(2, 1, key=3)) # initial=2
print(total(10, 1, 2, 3, vegetables=50, fruits=100)) 

