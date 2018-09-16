# gen_psw.py
import random

def gen_psw(num):
    '''
    Генератор паролей, где
    num - количество символов в пароле.
    '''
    s1 = '123456789'
    s2 = 'qwertyuiopasdfghjklzxcvbnm'
    s3 = s2.upper()
    s4 = s1 + s2 + s3
    ls = list(s4)
    random.shuffle(ls)
    return ''.join([random.choice(ls) for x in range(num)])

n = int(input("Сколько символов в пароле? "))
print(gen_psw(n))
