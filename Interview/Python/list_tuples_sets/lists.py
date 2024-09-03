courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[:2])
print(courses[2:])
print(courses[::-1])
courses.append('Art')
print(courses)
courses.insert(3, 'Biology')
print(courses)
courses2=['Education', 'PhysEd']
courses.extend(courses2)
print(courses)
courses.remove('Math')
print(courses)
pop = courses.pop()
print(courses)
print(pop)
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

#Without altering original
print(sorted(courses))

nums = [1,2,3,4,5,6,7]
print(min(nums))
print(max(nums))

ind = courses.index('Art')
print(ind)

print ('Art' in courses)
for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)

courses_str = ', '.join(courses)
print(courses_str)

courses1 = courses_str.split(',')
print(courses1)