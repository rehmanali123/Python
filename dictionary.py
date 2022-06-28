

student = {'name': 'John', 'age': 25, 'course': ['Maths', 'CS']}


student['phone'] = '555-5555'

print(student['name'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))


# update takes dictionary as an argument
student.update({'name':'Jane', 'age': 30})

print(student)

age = student.pop('age')

print("Popped value of age is : ", age)

print(student)
print("Length is: ", len(student))


# print out the keys and values separately

print(student.keys())
print(student.values())

# print out the whole key-value pair

print(student.items()) # return as a tuple


for key, values in student.items():
    print(key, values)


