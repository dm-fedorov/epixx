class Dog():
    name=""
    # Конструктор
    # Вызывается на момент создания объекта этого типа
    def __init__ (self, newName):
        self.name = newName

    # Можем в любой момент вызвать и изменить имя
    def setName (self, newName):
        self.name = newName
    # Можем в любой момент вызвать и узнать имя
    def getName (self):
        return self.name

# Создаем собаку
myDog = Dog ("Spot")

# Вывести имя собаки, убедиться, что оно было установлено
print (myDog.getName())

# Изменили имя собаки
myDog.setName("Sharik")

# Посмотрели изменения
print (myDog.getName())

