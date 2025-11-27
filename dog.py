class Dog:

    def __init__(self, name, age):
        self.Name = name 
        self.Age = age

    def get_age(self):
        return self.Age
    def get_name(self):
        return self.Name

d = Dog("Bill", 33)
b = Dog("Lassy", 20)
print(d.get_name(), d.get_age())
print(b.get_name(), d.get_age())

