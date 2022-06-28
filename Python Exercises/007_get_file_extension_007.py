# Write a Python program to accept a filename from the user and print the extension of that.


file_name = input("Input the file name : ")

file_ext = file_name.split('.')

print("File extension is : ", repr(file_ext[-1]))

