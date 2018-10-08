class Person():
    name=""
    def __init__ (self):
        print ("Создан человек")

class Employee (Person):
    job_title=""

class Customer (Person):
    email=""

johnSmith = Person()
janeEmployee = Employee()
bobCustomer = Customer()

