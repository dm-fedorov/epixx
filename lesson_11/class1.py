# class1.py
class Person:
    pass

# наследование полей класса Person
class Employee(Person):
    pass

class Customer(Person):
    pass

person = Person()
#person.name = "Иван Иванов"

emp = Employee()
emp.name = "Галина Семенова"
emp.job_title = "Web Developer"

cust = Customer()
cust.name = "Игорь Петров"
cust.email = "send_me@spam.com"

print(emp.name)
print(cust.name)
