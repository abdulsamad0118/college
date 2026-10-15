#  Positive Then Even Or Odd

n=int(input("Enter number: "))
if n>0:
     print("Positive even" if n%2==0 else "Positive odd")
elif n<0:
     print("Negative")
else: print("Zero")
