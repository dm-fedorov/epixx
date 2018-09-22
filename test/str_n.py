# str_n.py
def str_n(s, n):
    if len(s) > n:
          return s.upper()
     else:
          return s

if __name__ == "__main__":
     s = input("Введите строку: ")
     n = int(input("Введите число: "))
     print("Результат: ", str_n(s, n))

