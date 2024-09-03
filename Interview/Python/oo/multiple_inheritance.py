class Human():
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Dancer():
    def __init__(self, style):
        self.style = style

class Student(Human, Dancer):
    def __init__(self, age, name, style):
        Human.__init__(self, age, name)
        Dancer.__init__(self, style)

John = Student(20, "John", "HipHop")
print (John.name)
print(John.age)
print(John.style)
