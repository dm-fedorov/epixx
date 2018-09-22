# uncle.py
s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"

lst = s.split()

for i in lst:    
    if i.startswith('м'):
        lst.remove(i)

print(' '.join(lst))
