class Person():
    name=""
    def __init__(self):
        print ("Создан человек")

class Employee (Person):
    job_title=""
    def __init__(self):
        print ("Создан работник")

class Customer (Person):
    email=""
    def __init__(self):
        print ("Создан покупатель")

johnSmith = Person()
janeEmployee = Employee()
bobCustomer = Customer()
