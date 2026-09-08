#  Swap Two Numbers Using Bitwise

a=int(input("Enter a: "))
b=int(input("Enter b: "))
a=a^b
b=a^b
a=a^b
print(a,b)
