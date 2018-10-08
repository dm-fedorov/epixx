class Person():
    name=""

class Employee (Person):
    job_title=""

class Customer (Person):
    email=""

johnSmith = Person()
johnSmith.name = "John Smith"

janeEmployee = Employee()
janeEmployee.name = "Jane Employee"
janeEmployee.job_title = "Web Developer"

bobCustomer = Customer()
bobCustomer.name = "Bob Customer"
bobCustomer.email = "send_me@spam.com"

print(janeEmployee.name)
print(bobCustomer.name)
