
# LISTS IN PYTHON
# Remove,pop,insert,append,extend,join,split,max,min,sum,sorted,sort 



courses = ['chemistry', 'maths', 'physics', 'history']
# courses_2 = ['Art', 'Education']

print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])

print(courses[:2])

courses.append('CS')
courses.insert(0, 'Art')

print(courses)

# courses.insert(0, courses_2)

# courses.extend(courses_2)

courses.remove('maths')
popped = courses.pop()
print(courses)
print(popped)


# reverse the list
courses.reverse() # inplace reverse
print(courses)
courses.reverse()

print(courses)

courses.sort() # inplace sort
print("Sorted courses are: ", courses )

num = [ 2,5,8,9,4,6,3,7,8,6 ]
num.sort()  # sort in ascending order
print(num)

# sorting in descending order
# sort and reverse 

# 2 - descending order
num.sort(reverse=True)
print(num)

num = [543,652,85,996,453,34,42,23,54,65,456,2,32,3]
print(num)

sorted(num) # not in place sorted

print(sorted(num))

print(min(num))
print(max(num))
print(sum(num)) # sum of all numbers


# finding index of list element

fruits = ['apple', 'orange', 'grapes']

print(fruits.index('grapes'))


try:
    print(fruits.index('graes'))
except ValueError:
    print("element does not exist")



print('Art' in courses) # return True or False

for index, course in enumerate(courses, start = 1):
    print(index, course)


course_str = ', '.join(courses)
print(course_str)

print(course_str.split(','))


list1 = ['Chair', 'Bed', 'Sofa']
list2 = list1

print(list1)
print(list2)

list1.append('Mirror')

print(list2)







# Tuples... are ... immutable
# values cannot be changed...


vegetables = ('Potato', 'Tomato', 'Cabbage', 'Cucumber', 'Cabbage')

print(vegetables)

try:
    vegetables[0] = 'meat'
except:
    print("something went wrong assigining meat to vegetables")



# SETS ... unordered and have no duplicates


vegetables = {'Potato', 'Tomato', 'Cabbage', 'Cucumber'}

# sets are optimised for memebership tests
print('Tomato' in vegetables)


print(vegetables)

# creating empty list
empty_list = []
empty_list = list()

# creating empty tuple
empty_tuple = ()
empty_tuple = tuple()

# creating empty set
empty_set = set()

empty_dict = {} # empty dictionary


