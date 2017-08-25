
class Person:
    "person"
    def __init__(self, name,age,sex):
        self.name = name
        self.age=age
        self.sex=sex

    def getName(self):
        return self.name


p = Person("ny",18,"男")

#print(p.getName())
