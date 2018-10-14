# dog3.py
# Создаем описание собаки
class Dog:    
    # Конструктор
    # Вызывается в момент создания объекта этого типа
    def __init__(self, new_name='Собака без имени'):        
        self.name = new_name
    # Можем в любой момент вызвать этот метод и изменить имя:
    def setName(self, new_name):
        self.name = new_name
    # Можем в любой момент вызвать этот метод и узнать имя:
    def getName(self):
        return self.name

# Создаем конкретную собаку
my_dog = Dog("Тузик")
# Вывести имя собаки, убедиться, что оно было установлено
print(my_dog.getName())
# Изменили имя собаки
my_dog.setName("Шарик")
# Посмотрели изменения
print(my_dog.getName())

