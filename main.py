# Завдання 1

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")



# Створення екземпляра класу "Собака"
student1 = Student("Іван", 20)
student1.print_info()