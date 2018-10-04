# get_int.py
def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            return x            
        except ValueError:
            print("Error converting to a number")

print(get_int("Enter: "))
