# dog3.py
# Создаем описание собаки
class Dog():
    name = ""
    # Конструктор
    # Вызывается в момент создания объекта этого типа
    def __init__ (self, newName):
        self.name = newName
    # Можем в любой момент вызвать этот метод и изменить имя:
    def setName (self, newName):
        self.name = newName
    # Можем в любой момент вызвать этот метод и узнать имя:
    def getName (self):
        return self.name

# Создаем конкретную собаку
myDog = Dog("Тузик")
# Вывести имя собаки, убедиться, что оно было установлено
print(myDog.getName())
# Изменили имя собаки
myDog.setName("Шарик")
# Посмотрели изменения
print(myDog.getName())

