#  Largest Among Three

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

if a > b and a > c:
    print("Largest:", a)
elif b > a and b > c:
    print("Largest:", b)
else:
    print("Largest:", c)
