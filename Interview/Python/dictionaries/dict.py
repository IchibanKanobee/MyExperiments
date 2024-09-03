student = {'name': 'John', 'age': 25, 'cources':['Math', 'CompSci']}
print(student)
print(student['cources'])

#print(student['address'])
print (student.get('address'))

student['address'] = 'Here'
print (student.get('address'))

student.update({'name': 'Jane', 'age': 30, 'phone': '555-555-5555'})
print(student)

del student['age']
print(student)

cources = student.pop('cources')
print(student)

print (student.keys())
print(student.values())