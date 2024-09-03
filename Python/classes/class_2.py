class Person:
	def __init__(self):
		self.name = "Ara"
		self.age = 56
	'''		
	def __init__(self, name, age):
		self.name = name
		self.age = age
	'''
	def get_age():
		return self.age
	def set_age(age):
		self.age = age

class Student(Person):
	def __init__(self):
		Person.__init__(self)		
		self.school = "Chekhov"

p = Student()
print (p.school)
