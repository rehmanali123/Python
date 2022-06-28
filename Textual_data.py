
print("Hello World!")

message1 = "This is text example with double quotes"
message2 = 'This is text example with single quotes'

message3 = 'This is the example of "double quotes" within single quotes'
message4 = "This is the example of 'double quotes' within single quotes"

print(message1)
print(message2)
print(message3)
print(message4)


multi_line_string = """ 
This is multi line string 
example and can also be used for 
multi line comment
"""

print(multi_line_string)

# finding the length of the string

str_len = len(multi_line_string)
print('String length is : ', str_len)


# indexes of the string ...

sample_text = "This is the sample text"

# first index is included and last index is excluded
# slicing
print(sample_text[5:])


# string methods...

print(sample_text.lower())
print(sample_text.upper())

print(sample_text.count('.'))

print(sample_text.find('is')) # returns the index of searched keyword

replaced = sample_text.replace("text", "Paragraph") # replace is not in-place
print(replaced)


greeting = "Hello"
user = "User"

message = greeting + ", " + user

print(message)

# formatted string
message = '{}, {}. Welcome!'.format(greeting, user)
message = f'{greeting}, {user.upper()}. Welcome!'

print(message)



####
print(dir(message))

print('messageq'.islower())

# print(help(str))
# print(help(str.islower))










