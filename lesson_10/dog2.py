# dog2.py
class Dog:    
    # Конструктор
    # Вызывается на момент создания объекта этого типа
    def __init__ (self, new_name='Собака без имени'):
        self.name = new_name
        print("Родилась новая собака!")

# Создаем собаку
my_dog = Dog("Шарик")
# Вывести имя собаки, убедиться, что оно было установлено 
# (так обычно не делают!)
print(my_dog.name)
her_dog = Dog()
print(her_dog.name)
