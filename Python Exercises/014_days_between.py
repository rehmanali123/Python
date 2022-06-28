
# Write a Python program to calculate number of days between two dates.


from datetime import date

first = date(2014, 7, 2)
last  = date(2016, 3, 4)

delta = last - first

print(delta.days) 




