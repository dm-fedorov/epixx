# class_dog.py

def print_dog(dog):
    print(dog.name)

# Некоторая собака:
class Dog:    
    def bark(self): # Преобразуется в полную форму Dog.bark(myDog)
        self.age = 0
        self.name = ""
        self.weight = 0
        print("Гав-гав")        
    # метод для произношения имени:
    #def bark(self):
    #    print("Собака говорит: {0}".format(self.name))

# Конкретная собака:        
my_dog = Dog()
my_dog.name = "Шарик"
print(my_dog.name)
my_dog.weight = 20
my_dog.age = 3
my_dog.bark() # Преобразуется в полную форму Dog.bark(my_dog)
print_dog(my_dog)
