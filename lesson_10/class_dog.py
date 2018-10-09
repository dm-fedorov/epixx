# class_dog.py
# Некоторая собака:
class Dog():
    age = 0
    name = ""
    weight = 0
    def bark(self): # Преобразуется в полную форму Dog.bark(myDog)
        print("Woof")
    # метод для произношения имени:
    #def bark(self):
    #    print("Woof says",self.name)

# Конкретная собака:        
myDog = Dog()
myDog.name = "Spot"
myDog.weight = 20
myDog.age = 3
myDog.bark() # Преобразуется в полную форму Dog.bark(myDog)



