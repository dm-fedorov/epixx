# class_addr.py
# определяем шаблон адреса
class Address():
    name = ""
    line1 = ""
    line2 = ""
    city = ""
    state = ""
    zip1 = ""

# Создать экземпляр (объект) класса (типа) Address: 
homeAddress = Address()

# Задать поля объекта:
homeAddress.name = "John Smith"
homeAddress.line1 = "701 N. C Street"
homeAddress.line2 = "Carver Science Building"
homeAddress.city = "Indianola"
homeAddress.state = "IA"
homeAddress.zip = "50125"

# Создать еще один объекта типа Address:
vacationHomeAddress = Address()
# Задать поля этого адреса:
vacationHomeAddress.name = "John Smith"
vacationHomeAddress.line1 = "1122 Main Street"
vacationHomeAddress.line2 = ""
vacationHomeAddress.city = "Panama City Beach"
vacationHomeAddress.state = "FL"
vacationHomeAddress.zip = "32407"

print("The client's main home is in " + homeAddress.city)
print("His vacation home is in " + vacationHomeAddress.city)


