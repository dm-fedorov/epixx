# my_tasks.py
lst = []

def menu():
    print('''Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.
    ''')    

def add_task():
    task = []
    category = []
    t = input("Сформулируйте задачу: ")
    task.append(t)
    с = input("Добавьте категорию к задаче: ")
    task.append(с)
    tm = input("Добавьте время к задаче: ")
    task.append(tm)
    lst.append(task)
    
def print_list_task():
    if lst == []:
        print("Задач еще нет.")
    else:        
        for i in lst:
            print('Задача:', i[0], ' Категория:', i[1], " Дата:", i[2])
        #print(lst)

while True:
    menu()
    n = input("Укажите число: ")
    if n == '1':
        add_task()
    elif n == '2':
        print_list_task()
    elif n == '3':
        break

