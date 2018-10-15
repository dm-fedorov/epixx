# class_addr.py
# определяем шаблон адреса
class Address:
    pass
    
# Создать экземпляр (объект) класса (типа) Address: 
home = Address()

# Задать поля объекта:
home.name = "Иван Иванов"
home.line1 = "Улица"
home.line2 = "Район"
home.city = "СПб"
home.zip = "50125"

print("Город, где проживает {0} - {1} ".format(home.name, home.city))

