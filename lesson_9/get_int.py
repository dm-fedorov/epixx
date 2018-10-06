# get_int.py
def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            return x            
        except ValueError:
            print("Error converting to a number")

if __name__ == "__main__":
    print(get_int("Enter: "))
