# count_num.py
s='aa3aBbb6ccc'
total=0
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total=total+int(s[i])

print ("сумма чисел:", total)
