# class2.py
class Person():    
    def __init__(self, name=''):
        print("Создан человек")
        self.name = name

class Employee(Person):
    job_title = ""

class Customer(Person):
    email = ""

johnSmith = Person('123')
janeEmployee = Employee()
bobCustomer = Customer()
print(bobCustomer.name)
