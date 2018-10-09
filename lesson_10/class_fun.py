# class_fun.py
# Обновленная функция, которая обрабатывает объект типа (класса) Address.
# Вывести адрес на экран:
def print_address(address):
    print(address.name)
    if len(address.line1) > 0:
        print(address.line1)
    if len(address.line2) > 0:
        print(address.line2)
    print(address.city + ", " + address.state + " " + address.zip)

if __name__ == '__main__':
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

    print_address(homeAddress)

