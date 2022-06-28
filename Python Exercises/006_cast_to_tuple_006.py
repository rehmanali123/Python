
# Write a Python program which accepts a sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers.

values = input("Input some comma separated values: ")

numbers = values.split(',')

print(list(numbers))
print(tuple(numbers))