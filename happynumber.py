n = int(input("enter a number : "))



while n != 1 and n != 4:
    sum = 0 

    while n > 0:

     lt = n % 10 
     sum = sum + lt**n
     n = n // 10 

    n = sum 


if n == 1:
    print("Happy number")
else:
    print("Not a happy number")