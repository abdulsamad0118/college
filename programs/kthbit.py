#  Kth Bit Set Or Not

n=int(input("Enter number: "))
k=int(input("Enter bit position: "))
if n&(1<<k) :
    print("set")
else:
 print("notset")
