# err1.py
try:
    x = int(input("Enter number: "))
    print(5/x)
except ZeroDivisionError:
    print("Error dividing by zero")
except ValueError:
    print("Error converting to a number")
