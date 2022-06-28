 # Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.


n = input("Enter the number : ")

n1 = int(n)
n2 = int("%s%s" %(n,n))
n3 = int("%s%s%s" %(n,n,n))

n = n1 + n2 + n3

print(n)



